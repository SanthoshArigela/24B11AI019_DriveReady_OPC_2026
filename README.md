# Medivora AI

**Intelligent Pharmacy. Better Operations.**

Medivora AI is a proposed B2B HealthTech startup building an AI operations copilot for independent pharmacies in India. This repository is the Drive Ready OPC 2026 learning and product-discovery workspace of Arigela Tejasri Sai Santhosh (24B11AI019).

## Problem and product
Pharmacy staff may struggle with fragmented stock, batch expiry, purchasing and sales records. Medivora Copilot aims to make these records searchable and actionable with source-backed AI assistance. These are hypotheses to validate through interviews and a pilot.

## Initial MVP
Staff question → intent extraction → validated inventory lookup → deterministic stock/expiry analysis → grounded answer → staff review → audit record.

Planned capabilities: inventory lookup, low-stock alerts, batch expiry reporting, natural-language sales summaries and draft reorder lists. Later: invoice OCR and demand forecasting.

## Status
**Proposed concept; implementation not yet verified.** No live pharmacy integrations, clinical capabilities, customer data or commercial launch. Day folders below are planned, not completed. The company name and legal structure are unverified.

## Drive Ready learning plan
| Day | Learning topic | Planned Medivora application |
|---|---|---|
| 01 | LLM chatbot | Pharmacy operations chatbot with no live data |
| 02 | Prompt engineering and Python | Structured inventory intent, JSON validation and error handling |
| 03 | Basic LangChain agent | Pharmacy operations assistant; ten scenario tests |

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
Day-01/task.py, README.md
Day-02/task.py, README.md
Day-03/task.py, README.md, test.csv
docs/
src/
tests/
requirements.txt
.env.example
.gitignore
```
Only documentation and starter configuration are provided in this package. No executable daily submissions are represented as complete.

## Setup (for future implementations)
Use Python in a virtual environment or Google Colab. Install dependencies after the actual assignment and provider are confirmed. Store API keys in environment variables or Colab Secrets. Never commit credentials, prescriptions or identifiable customer data.

## Principles
Use deterministic code for inventory, arithmetic and dates; use LLMs for language understanding and explanation. Show record IDs, freshness and missing-data warnings. Require authorized human approval for consequential changes. No diagnosis, prescribing, dosage advice or automatic medicine substitution. No claims of compliance or business impact without verification.
