# Day 04 — Tools, structured output and Google Sheets

Faculty sources: Day 4 HTML tutorial and AI_Agent.ipynb. Adapted bakery tools to synthetic pharmacy inventory. Default GPT-OSS-20B follows HTML and Day 03.

## Run in Colab
Open [notebook](https://colab.research.google.com/github/SanthoshArigela/24B11AI019_DriveReady_OPC_2026/blob/main/Day-04/Medivora_AI_Day_04.ipynb). Run setup, definitions, data, local assertions, model initialization, structured extraction, evaluation and naming experiment. Enable GROQ_API_KEY in Secrets for this notebook. Optional Google authentication creates a private demo sheet or reuses its ID. Review extracted fields and type SAVE to approve the exact draft. Use fictional names only. Interactive chat is read-only unless a trusted approval is active; exit to stop.

## Assignment mapping
- Two Day 03 functions converted to @tool; price and synthetic stock.
- Pydantic ReorderRequest and five messy messages using with_structured_output.
- Google Sheets log_reorder with exact-record approval, RAW cell values and no automatic retry on writes.
- Clear → vague tool1 → restored naming experiment and trace counts.
- Extended Day 03 CSV with seven cases, including unknown item, missing date and zero quantity.
- Twenty business facts for Day 05 RAG.

## Safety and limitations
No live inventory, clinical advice or actual purchasing. Single-session approval and duplicate-attempt protection are not a distributed idempotency guarantee. If a sheet write fails, inspect request ID before retrying. Structured extraction must be reviewed; schema alone cannot prove source fidelity. Keyword tests are approximate; inspect traces and actual answers. API retry applies to read-only experiments, not approved writes. Results are generated only on execution; no fabricated pass rates.

## Files
task.py contains the full implementation, tests.csv and structured_output_tests.csv contain fixtures, business_facts.txt is the RAG seed. Notebook embeds all fixtures and code. Actual CSV outputs: day04_agent_results.csv, day04_structured_results.csv, day04_naming_results.csv.

## Status
Source prepared; live Groq and Google Sheets execution pending.
