# Day 02 — Prompts, memory and the Python agents need

Faculty tutorial: Day 2, Level 1 Fundamentals. Adapted from Sweet Crumbs to Medivora AI. All catalogue entries and prices are synthetic, not medicine prices or actual inventory. No real ordering, live stock or clinical advice.

## Run
Open [Colab notebook](https://colab.research.google.com/github/SanthoshArigela/24B11AI019_DriveReady_OPC_2026/blob/main/Day-02/Medivora_AI_Day_02.ipynb). Enable GROQ_API_KEY in Colab Secrets; run cells in order. Locally install root requirements and run python Day-02/task.py. Type exit to finish the interactive chatbot.

## Faculty assignment
| Task | Implementation |
|---|---|
| Messages and roles, Role/Facts/Rules/Format | SYSTEM and msg |
| Prompt parts | prompt_experiment: rules removed/restored, installation in one hour |
| Few-shot | 3 examples, 5 held-out messages, zero-shot versus few-shot |
| JSON | name/item/qty/date/urgent, json.loads, validation and try/except |
| Memory | MAX_TURNS 8 versus 2, synthetic name then three turns |
| Dict, function, type hints, decorator | CATALOGUE, get_price, log_call |
| Error handling and chat loop | ChatSession, interactive |

The bakery's eggless field is replaced with urgent, a pharmacy draft-request field. MAX_TURNS follows the faculty's message-count convention; it is not a token budget. The system prompt is retained. The deterministic price function is demonstrated separately, not connected as an agent tool.

## Catalogue (synthetic INR/unit)
- demo product a: 50
- demo product b: 120
- demo product c: 80

Expected deterministic total for two units of demo product b: INR 240. Model outputs must be observed, not assumed.

## Day 03 preparation
Bring the above Python catalogue and the [ten Day 01 FAQs](../Day-01/README.md).

## Results
Source and notebook prepared. Live API execution and results pending. Record actual outputs, classifier counts, JSON result, rule comparison and memory behavior after execution. The revised Day 01 prompt remains separately pending live regression testing.
