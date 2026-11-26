# Day 03 — Your first agent and LangChain

Adapted from the faculty HTML tutorial, combined Day 1–3 notebook and sample test.csv. The HTML uses gpt-oss-20b, the faculty notebook uses gpt-oss-120b; this implementation defaults to 20b for continuity with Medivora, configurable via GROQ_MODEL.

## Run
Open the Colab notebook, enable GROQ_API_KEY access and run sequentially. Notebook embeds the adapted tests.csv so no upload is needed. Locally install root requirements then run python Day-03/task.py. Optional interactive cell: type exit to stop.

## Assignment mapping
- ChatPromptTemplate, MessagesPlaceholder, ChatGroq and StrOutputParser: LCEL chain and bounded message history.
- Ten Day 01 FAQs: tests.csv, matching faculty's question/must_include columns.
- Baseline 0.3, improved prompt 0.3, improved 1.0 twice: four runs, 40 test cases. Improvement adds explicit English status language; same questions and rubric across runs. This tunes wording against the test set, not an independent generalization benchmark.
- Empty responses and transient errors: bounded retry; per-case errors are recorded, not made up.
- create_agent with tools=[]: preview only, no autonomous tool calls. Actual tools scheduled for Day 04.
- Day 04 preparation: typed get_price and is_available functions with docstrings; synthetic catalogue only.
- Actual results: generated locally as day03_actual_results.csv after execution. No observed pass rates yet.

## Agent or not?
| Business job | Approach |
|---|---|
| Compute catalogue quantity × unit price | Plain code |
| Draft a pharmacy operations product introduction | One LLM call |
| Investigate low-stock records, check batch information and draft a replenishment recommendation with approval | Agent (future tools and authorized data required) |

## Evaluation limitations
Substring matches follow the faculty method; they cannot prove factual correctness, safety or meaningful improvement. Manually review answers and compare both temperature runs. Failed requests count as not passed and are flagged incomplete. No real pharmacy data, purchases, clinical advice or actual stock access.

## Status
Implementation prepared; live API execution pending. Day 02 execution was reported complete by the student but detailed outputs have not been verified.
