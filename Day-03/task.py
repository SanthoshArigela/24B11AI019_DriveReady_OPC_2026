"""Day 03: LangChain assistant, evaluation and agent preview."""
import os
import csv
import io
import time
from pathlib import Path
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain.agents import create_agent
from groq import APIError, APIConnectionError, RateLimitError

MODEL = os.getenv("GROQ_MODEL", "openai/gpt-oss-20b")
CATALOGUE = {"demo product a": 50, "demo product b": 120, "demo product c": 80}
SYSTEM = """ROLE: You are Medivora AI's friendly pharmacy operations assistant.
FACTS: Medivora is a learning prototype intended for independent pharmacies.
Low-stock alerts, batch expiry, sales reports, reorder drafts and role-based store isolation are planned, not implemented.
There is no live inventory. Billing integration and subscription pricing are not confirmed.
The fictional demo catalogue has unit prices A=50, B=120, C=80 INR.
RULES: Clearly distinguish planned features from actual capabilities. Never invent records, prices, services or completed actions.
No clinical advice, prescribing, dosage or substitution. Refer clinical questions to a pharmacist. Never execute purchases.
FORMAT: Friendly English or Telugu matching the user, under 50 words."""
IMPROVED_SYSTEM = SYSTEM + """
For English enquiries, use explicit status language: 'planned' for future features,
'no live' for unavailable live inventory, and 'not confirmed' for unknown commercial details.
Identify Medivora as a prototype. Do not imply future capabilities already exist."""

def get_key() -> str:
    key = os.getenv("GROQ_API_KEY")
    if not key:
        try:
            from google.colab import userdata
            key = userdata.get("GROQ_API_KEY")
        except Exception:
            pass
    if not key:
        raise RuntimeError("Enable GROQ_API_KEY in Colab Secrets or environment.")
    return key

def make_model(temperature: float = 0.3):
    return ChatGroq(model=MODEL, temperature=temperature, api_key=get_key(),
                    max_retries=0, timeout=30)

def make_chain(system: str = SYSTEM, temperature: float = 0.3):
    prompt = ChatPromptTemplate.from_messages([
        ("system", system), MessagesPlaceholder("history"),
        ("human", "{question}"),
    ])
    return prompt | make_model(temperature) | StrOutputParser()

def invoke_text(call) -> str:
    for attempt in range(1, 4):
        try:
            answer = call()
            if isinstance(answer, str) and answer.strip():
                return answer.strip()
            error = ValueError("Empty final model response")
        except APIConnectionError as exc:
            error = exc
        except APIError as exc:
            status = getattr(exc, "status_code", None)
            if not isinstance(exc, RateLimitError) and status not in (408, 409, 429) and not (isinstance(status, int) and status >= 500):
                raise
            error = exc
        if attempt == 3:
            raise error
        print(f"[retry {attempt}/2] {type(error).__name__}")
        time.sleep(attempt)
    raise AssertionError("Unreachable")

class Assistant:
    def __init__(self, chain):
        self.chain = chain
        self.history = []

    def ask(self, question: str) -> str:
        answer = invoke_text(lambda: self.chain.invoke(
            {"history": self.history[-8:], "question": question}))
        self.history.extend([("human", question), ("ai", answer)])
        self.history = self.history[-8:]
        return answer

def run_tests(chain, path: str, label: str) -> list[dict]:
    with open(path, encoding="utf-8", newline="") as file:
        rows = list(csv.DictReader(file))
    if not rows or any(not row.get("question") or not row.get("must_include") for row in rows):
        raise ValueError("Test CSV must contain question and must_include.")
    results = []
    for row in rows:
        try:
            answer = invoke_text(lambda: chain.invoke(
                {"history": [], "question": row["question"]}))
            status = "PASS" if row["must_include"].casefold() in answer.casefold() else "FAIL"
        except (APIError, ValueError) as exc:
            answer = ""
            status = "ERROR:" + type(exc).__name__
        record = {"run": label, **row, "answer": answer, "status": status}
        results.append(record)
        print(status, "|", row["question"], "->", answer or "(no answer)")
    passed = sum(row["status"] == "PASS" for row in results)
    errors = sum(row["status"].startswith("ERROR") for row in results)
    print(f"{label}: {passed}/{len(rows)} passed ({passed/len(rows):.0%}); {errors} errors")
    if errors:
        print("Incomplete evaluation; rerun before drawing final conclusions.")
    return results

def evaluate(path: str) -> list[dict]:
    results = []
    for label, system, temp in [
        ("baseline_0.3", SYSTEM, 0.3),
        ("improved_0.3", IMPROVED_SYSTEM, 0.3),
        ("improved_1.0_run1", IMPROVED_SYSTEM, 1.0),
        ("improved_1.0_run2", IMPROVED_SYSTEM, 1.0),
    ]:
        print("\n---", label, "---")
        results.extend(run_tests(make_chain(system, temp), path, label))
    with open("day03_actual_results.csv", "w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["run", "question", "must_include", "answer", "status"])
        writer.writeheader()
        writer.writerows(results)
    for label in dict.fromkeys(row["run"] for row in results):
        group = [row for row in results if row["run"] == label]
        print(label, sum(row["status"] == "PASS" for row in group), "/", len(group))
    print("Saved day03_actual_results.csv; substring checks are not full factual or safety evaluations.")
    return results

def demo():
    assistant = Assistant(make_chain())
    for question in ["Hi, my name is Ravi.", "What's my name?",
                     "Can you install Medivora today?", "What is the demo price for 6 units of product C?"]:
        try:
            print("You:", question, "\nBot:", assistant.ask(question))
        except (APIError, ValueError) as exc:
            print("[ERROR]", type(exc).__name__)

def agent_preview():
    agent = create_agent(model=make_model(), tools=[], system_prompt=IMPROVED_SYSTEM)
    question = "Can you check my real pharmacy stock?"
    answer = invoke_text(lambda: agent.invoke(
        {"messages": [{"role": "user", "content": question}]},
        config={"recursion_limit": 10})["messages"][-1].content)
    print("Agent preview:", answer)

def get_price(item: str, qty: int = 1) -> int:
    """Calculate fictional total INR for a catalogue item and positive integer quantity."""
    if type(qty) is not int or qty <= 0:
        raise ValueError("Quantity must be a positive integer")
    return CATALOGUE[item.strip().lower()] * qty

def is_available(item: str) -> bool:
    """Check fictional catalogue membership, not real pharmacy stock availability."""
    return item.strip().lower() in CATALOGUE

def tool_demo():
    assert get_price("demo product b", 2) == 240
    assert is_available("demo product c")
    assert not is_available("unknown")
    print("Synthetic total:", get_price("demo product b", 2))
    print("Catalogue membership:", is_available("demo product c"), is_available("unknown"))

def interactive():
    assistant = Assistant(make_chain(IMPROVED_SYSTEM))
    while True:
        try:
            question = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            break
        if question.lower() in ("exit", "quit", "bye"):
            break
        if question:
            try:
                print("Bot:", assistant.ask(question))
            except (APIError, ValueError) as exc:
                print("[ERROR]", type(exc).__name__)

def main():
    demo()
    evaluate(str(Path(__file__).with_name("tests.csv")))
    agent_preview()
    tool_demo()

if __name__ == "__main__":
    main()
