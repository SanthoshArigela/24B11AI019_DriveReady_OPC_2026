# Medivora AI

**Intelligent Pharmacy. Better Operations.**

Medivora AI is a proposed B2B HealthTech startup building an AI operations copilot for independent pharmacies in India. This repository is the Drive Ready OPC 2026 learning and product-discovery workspace of Arigela Tejasri Sai Santhosh (24B11AI019).

## Problem and product
Pharmacy staff may struggle with fragmented stock, batch expiry, purchasing and sales records. Medivora Copilot aims to make these records searchable and actionable with source-backed AI assistance. These are hypotheses to validate through interviews and a pilot.

## Initial MVP
Staff question → intent extraction → validated inventory lookup → deterministic stock/expiry analysis → grounded answer → staff review → audit record.

Planned capabilities: inventory lookup, low-stock alerts, batch expiry reporting, natural-language sales summaries and draft reorder lists. Later: invoice OCR and demand forecasting.

## Status
**Proposed concept; implementation not yet verified.** No live pharmacy integrations, clinical capabilities, customer data or commercial launch. Day 01 original learning prototype executed successfully in Colab; screenshot-backed results are recorded. Revised prompt v2 awaits live regression testing. Day 02 execution reported complete by the student; detailed results pending. Day 03 agent execution reported working; full evaluation evidence pending. Day 04 implementation committed; live Groq and Sheets tests pending. The company name and legal structure are unverified.

## Drive Ready learning plan
| Day | Learning topic | Planned Medivora application |
|---|---|---|
| 01 | LLM chatbot | [Pharmacy operations chatbot and experiments](Day-01/README.md) — v1 executed; v2 retest pending |
| 02 | Prompt engineering and Python | [Context-aware chatbot, few-shot classification and JSON](Day-02/README.md) — live execution pending |
| 03 | Basic LangChain agent | [LangChain assistant and ten FAQ tests](Day-03/README.md) — live execution pending |

| 04 | Tools, structured output and Google Sheets | [Synthetic inventory and approved reorder drafts](Day-04/README.md) — live execution pending |

Later learning topics will follow the mentor's actual curriculum rather than an assumed schedule.

## Documentation
- [Company profile](docs/COMPANY_PROFILE.md)
- [Product vision](docs/PRODUCT_VISION.md)
- [Business model](docs/BUSINESS_MODEL.md)
- [System architecture](docs/SYSTEM_ARCHITECTURE.md)
- [Development roadmap](docs/DEVELOPMENT_ROADMAP.md)
- [Security and safety](docs/SECURITY_POLICY.md)
- [MVP acceptance tests](docs/MVP_TEST_PLAN.md)

## Planned repository layout
```text
Day-01/task.py, README.md, Medivora_AI_Day_01.ipynb, EXPERIMENT_RESULTS.md, test_results.csv
Day-02/task.py, README.md, Medivora_AI_Day_02.ipynb
Day-03/task.py, README.md, tests.csv, Medivora_AI_Day_03.ipynb
Day-04/task.py, README.md, tests.csv, structured_output_tests.csv, business_facts.txt, Medivora_AI_Day_04.ipynb
docs/
src/
tests/
requirements.txt
.env.example
.gitignore
```
Day 01 source, notebook and dependencies are available. See [actual experiment results](Day-01/EXPERIMENT_RESULTS.md) and [CSV](Day-01/test_results.csv). Day 02 execution reported complete; outputs pending verification. Day 03 implementation is ready for live evaluation.

## Setup (for future implementations)
Use Python in a virtual environment or Google Colab. Install Day 01 dependencies using `pip install -r requirements.txt`. See [Day 01 instructions](Day-01/README.md). Store API keys in environment variables or Colab Secrets. Never commit credentials, prescriptions or identifiable customer data.

## Principles
Use deterministic code for inventory, arithmetic and dates; use LLMs for language understanding and explanation. Show record IDs, freshness and missing-data warnings. Require authorized human approval for consequential changes. No diagnosis, prescribing, dosage advice or automatic medicine substitution. No claims of compliance or business impact without verification.

## Day 04 observed results and final revision
Original 8/17; revised 12/17; structured 5/5; no revised API errors. See Day-04/EXPERIMENT_RESULTS.md. V3 code committed; live retest and Google Sheets write evidence pending. New output filenames end in _v3.csv.

## Day 05 transition
Day 04 runtime and Sheets verification confirmed by user; exact V3 score not supplied. Day 05 memory and RAG implementation committed; live evaluation pending. See Day-05/README.md.
