# Development roadmap

Day 01 original learning prototype executed and documented on 26 November 2026. Revised prompt v2 is implemented but not yet live-tested. Other phases remain planned. Confirm daily assignments against mentor instructions.

| Phase | Deliverable | Exit criteria |
|---|---|---|
| 0 | Day 1 chatbot, Day 2 prompts/Python, Day 3 agent | Source files and actual test outcomes recorded; no invented stock |
| 1 | Customer discovery and sample schema | 5–10 interviews, workflow selected, data permission defined |
| 2 | CSV inventory tools | Validate quantities, product identity, batch expiry, timestamps; test edge cases |
| 3 | Grounded assistant | Tool-based answers with IDs, freshness, missing-data fallback |
| 4 | Pilot backend and dashboard | Authentication, store isolation, audit, backup and approved writes |
| 5 | Controlled pharmacy pilot | Authorized records, pharmacist review, measured baseline and outcomes |
| 6 | Invoice OCR and forecasting | Human verification, forecast backtest versus naive baseline |
| 7 | Commercial readiness | Pricing validation, support plan, security and legal review |

Faculty-confirmed Day 04: tool calling, structured outputs and Google Sheets. Day 05 preparation: 20 business facts for RAG. Later topics remain unconfirmed.

## Release gates
No real customer pilot without authorization, access controls, tested expiry/stock logic, secret management, manual fallback, audit and data retention policy. No autonomous medicine sales or purchasing.

## Phase 0 progress
- [x] Day 01 source and notebook
- [x] Original live API experiments (student screenshots)
- [x] [Results documented](../Day-01/EXPERIMENT_RESULTS.md) and [CSV](../Day-01/test_results.csv)
- [x] Revised grounding prompt in both source and notebook
- [ ] Live regression test of v2 (planned capabilities, nonexistent dashboard/sales team, stock and clinical boundaries)
- [x] Day 02 prompt engineering and Python source and notebook
- [ ] Day 02 live experiments and observations (student reports completion; evidence pending)
- [x] Day 03 LangChain assistant, no-tool agent preview and ten FAQ tests
- [ ] Day 03 live evaluation (four runs)
- [x] Day 04 preparation: two synthetic catalogue functions
- [x] Day 04 tools, Pydantic, approved draft logging, notebook and test fixtures
- [ ] Day 04 live Groq evaluation and Google Sheets write verification
- [x] Day 05 RAG preparation: 20 synthetic business facts
- [x] Day 04 debugging revision and original 8/17 screenshot baseline preserved
- [ ] Day 04 revised live evaluation and Google Sheets verification

## Day 04 observed results and final revision
Original 8/17; revised 12/17; structured 5/5; no revised API errors. See Day-04/EXPERIMENT_RESULTS.md. V3 code committed; live retest and Google Sheets write evidence pending. New output filenames end in _v3.csv.
