"""Medivora Day 04: synthetic inventory and human-approved draft logging."""
import os, time, csv, json, uuid
from datetime import date
from typing import Literal
from pydantic import BaseModel, Field, ConfigDict, ValidationError
from langchain.tools import tool
from langchain.agents import create_agent
from langchain_groq import ChatGroq
from groq import APIConnectionError, APIStatusError

CATALOGUE = {"demo product a": (50,100), "demo product b": (120,25), "demo product c": (80,0)}
SYSTEM = """You are Medivora AI, a prototype for independent pharmacies.
Use get_price for prices and is_available for demo stock. Never claim live stock.
Low-stock alerts, batch expiry, sales reports and store isolation are planned.
Billing integration and subscription price are not confirmed. Reorder drafts only.
Never invent facts, clinical advice, purchases or saved records. Ask for missing fields.
A draft requires staff name, catalogue item, positive quantity, ISO date and priority.
Use log_reorder only after explicit approval; the program independently enforces approval.
Reply briefly in English or Telugu matching the user."""

class ReorderRequest(BaseModel):
    model_config = ConfigDict(extra="forbid", str_strip_whitespace=True)
    staff_name: str = Field(min_length=1, max_length=80)
    item: Literal["demo product a","demo product b","demo product c"]
    qty: int = Field(strict=True, ge=1, le=10000)
    required_date: date
    priority: Literal["normal","urgent"]

def get_key():
    key = os.getenv("GROQ_API_KEY")
    if not key:
        try:
            from google.colab import userdata
            key = userdata.get("GROQ_API_KEY")
        except Exception as exc:
            raise RuntimeError("Enable GROQ_API_KEY in this notebook's Secrets.") from exc
    if not key:
        raise RuntimeError("GROQ_API_KEY is missing.")
    return key

def make_model():
    return ChatGroq(model=os.getenv("GROQ_MODEL","openai/gpt-oss-20b"),
                    api_key=get_key(), temperature=0.2, max_retries=0, timeout=45)

def retry_read(call):
    for attempt in range(3):
        try:
            result = call()
            if result is None or (isinstance(result,str) and not result.strip()):
                raise ValueError("Empty response")
            return result
        except (APIConnectionError, APIStatusError, ValueError) as exc:
            if isinstance(exc, APIStatusError) and exc.status_code not in (408,409,429) and exc.status_code < 500:
                raise
            if attempt == 2:
                raise
            time.sleep(2 ** attempt)

@tool
def get_price(item: str, qty: int = 1) -> str:
    """Calculate exact synthetic INR total for demo product a, b or c and positive quantity."""
    item = item.strip().lower()
    if item not in CATALOGUE:
        return "Unknown product; use demo product a, b or c."
    if type(qty) is not int or not 1 <= qty <= 10000:
        return "Invalid quantity; enter a positive integer up to 10000."
    return f"Demo total: INR {CATALOGUE[item][0]*qty}"

@tool
def is_available(item: str) -> str:
    """Check synthetic stock count for demo product a, b or c; not live pharmacy stock."""
    item = item.strip().lower()
    if item not in CATALOGUE:
        return "Unknown product."
    stock = CATALOGUE[item][1]
    return f"Demo stock: {stock} units" if stock else "Out of stock in demo inventory (0 units)."

HEADERS = ["request_id","staff_name","item","qty","required_date","priority","total_inr","status"]

class DraftStore:
    def __init__(self, worksheet=None):
        self.ws = worksheet
        self.rows = []
        self.approved = None
        self.attempted = set()

    def approve(self, record):
        """Called only by trusted UI after human reviews exact record."""
        self.approved = (uuid.uuid4().hex, record.model_dump(mode="json"))

    def save(self, record):
        if not self.approved or self.approved[1] != record.model_dump(mode="json"):
            return "Not saved: exact draft requires human approval."
        rid, _ = self.approved
        self.approved = None
        if rid in self.attempted:
            return "Not saved: duplicate attempt."
        self.attempted.add(rid)
        row = [rid,record.staff_name,record.item,record.qty,record.required_date.isoformat(),
               record.priority,CATALOGUE[record.item][0]*record.qty,"DRAFT"]
        if self.ws is not None:
            try:
                self.ws.append_row(row, value_input_option="RAW")
            except Exception:
                return f"Write outcome uncertain; inspect sheet for {rid} before retrying."
        self.rows.append(row)
        return f"Saved {'Google Sheets' if self.ws is not None else 'local demo'} draft {rid}; INR {row[6]}. No purchase executed."

def connect_sheet():
    from google.colab import auth
    from google.auth import default
    import gspread
    auth.authenticate_user()
    gc = gspread.authorize(default()[0])
    sid = input("Existing spreadsheet ID (blank to create a new demo sheet): ").strip()
    sh = gc.open_by_key(sid) if sid else gc.create("Medivora AI - Reorder Requests")
    ws = sh.sheet1
    existing = ws.row_values(1)
    if not existing:
        ws.append_row(HEADERS, value_input_option="RAW")
    elif existing != HEADERS:
        raise ValueError("Unexpected sheet headers; choose a dedicated demo sheet.")
    print("Sheet:", sh.url)
    return DraftStore(ws)

def make_agent(llm, store, vague=False):
    @tool
    def log_reorder(staff_name: str, item: str, qty: int, required_date: str, priority: str) -> str:
        """Save only an exact human-approved synthetic reorder draft; requires all five fields."""
        try:
            record = ReorderRequest(staff_name=staff_name,item=item.strip().lower(),
                qty=qty,required_date=required_date,priority=priority)
        except ValidationError:
            return "Not saved: invalid or missing reorder fields."
        return store.save(record)
    @tool
    def tool1(item: str, qty: int = 1) -> str:
        """does stuff"""
        return get_price.invoke({"item":item,"qty":qty})
    return create_agent(model=llm, tools=[tool1 if vague else get_price,is_available,log_reorder],
                        system_prompt=SYSTEM)

def run_agent(agent, question, history=None, trace=False, read_only=False):
    messages = list(history or []) + [{"role":"user","content":question}]
    def invoke():
        result = agent.invoke({"messages":messages},config={"recursion_limit":16})
        if not result["messages"][-1].content:
            raise ValueError("Empty final response")
        return result
    result = retry_read(invoke) if read_only else invoke()
    new = result["messages"][len(messages):]
    calls = [c["name"] for m in new for c in getattr(m,"tool_calls",[])]
    rounds = sum(m.type=="ai" for m in new)
    if trace:
        for m in new:
            m.pretty_print()
        print("Tool calls:",calls,"Model calls:",rounds)
    return result["messages"][-1].content, result["messages"], calls, rounds

def extract(llm, message):
    extractor = llm.with_structured_output(ReorderRequest)
    return retry_read(lambda: extractor.invoke([
        ("system","Extract only explicitly supplied fields. Never invent missing values. Use ISO dates and canonical demo product names."),
        ("human",message)]))

def structured_tests(llm, path="structured_output_tests.csv"):
    results=[]
    with open(path,encoding="utf-8") as f:
        for row in csv.DictReader(f):
            try:
                actual=extract(llm,row["message"]).model_dump(mode="json")
                status="PASS" if actual==json.loads(row["expected_json"]) else "FAIL"
            except Exception as exc:
                actual={"error":type(exc).__name__}
                status="ERROR"
            results.append({**row,"actual":json.dumps(actual),"status":status})
            print(status,actual)
    write_csv("day04_structured_results.csv",results)

def write_csv(path, rows):
    if rows:
        with open(path,"w",encoding="utf-8",newline="") as f:
            writer=csv.DictWriter(f,fieldnames=list(rows[0]))
            writer.writeheader()
            writer.writerows(rows)

def evaluate(llm,path="tests.csv"):
    store=DraftStore()
    agent=make_agent(llm,store)
    results=[]
    with open(path,encoding="utf-8") as f:
        for row in csv.DictReader(f):
            try:
                answer,_,calls,rounds=run_agent(agent,row["question"],read_only=True)
                status="PASS" if row["must_include"].casefold() in str(answer).casefold() and not store.rows else "FAIL"
            except Exception as exc:
                answer=type(exc).__name__
                calls,rounds,status=[],0,"ERROR"
            results.append({**row,"answer":str(answer),"tools":json.dumps(calls),"model_calls":rounds,"status":status})
            print(status,row["question"],answer)
    write_csv("day04_agent_results.csv",results)
    print("Passed:",sum(r["status"]=="PASS" for r in results),"/",len(results))

def naming_experiment(llm):
    rows=[]
    for vague in (False,True,False):
        try:
            answer,_,calls,rounds=run_agent(make_agent(llm,DraftStore(),vague),
                "What is the price of 5 units of demo product b?",trace=True,read_only=True)
            rows.append({"vague":vague,"answer":str(answer),"tools":json.dumps(calls),"model_calls":rounds})
        except Exception as exc:
            rows.append({"vague":vague,"answer":type(exc).__name__,"tools":"[]","model_calls":0})
    write_csv("day04_naming_results.csv",rows)

def review_and_save(llm,store,message):
    record=extract(llm,message)
    print(record.model_dump_json(indent=2))
    print("Total INR:",CATALOGUE[record.item][0]*record.qty)
    if input("Type SAVE to approve this exact synthetic draft: ").strip()!="SAVE":
        print("Cancelled; nothing saved.")
        return
    store.approve(record)
    try:
        answer,_,_,_=run_agent(make_agent(llm,store),
            "Call log_reorder for this approved exact draft: "+record.model_dump_json(),trace=True)
        print(answer)
    finally:
        store.approved=None

def self_test():
    assert "600" in get_price.invoke({"item":"demo product b","qty":5})
    assert "Unknown" in get_price.invoke({"item":"x"})
    assert "Invalid" in get_price.invoke({"item":"demo product a","qty":0})
    assert "Out of stock" in is_available.invoke({"item":"demo product c"})
    record=ReorderRequest(staff_name="Demo Ravi",item="demo product b",qty=5,required_date="2026-12-05",priority="normal")
    store=DraftStore()
    assert "Not saved" in store.save(record)
    store.approve(record)
    assert "Saved" in store.save(record)
    assert "Not saved" in store.save(record)
    assert len(store.rows)==1 and store.rows[0][6]==600
    print("Local assertions passed.")

def interactive(llm,store):
    agent=make_agent(llm,store)
    history=[]
    while True:
        question=input("You (exit to stop): ").strip()
        if question.lower() in ("exit","quit","bye"):
            break
        try:
            answer,history,_,_=run_agent(agent,question,history)
            print("Bot:",answer)
        except Exception as exc:
            print("Agent error:",type(exc).__name__)
