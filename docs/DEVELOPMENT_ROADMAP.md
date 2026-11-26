# Development roadmap

All items are planned, not completed. Confirm daily assignments against mentor instructions.

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

Future optional topics: tool calling, memory, embeddings/RAG, structured outputs, deployment and multi-agent orchestration. These are not confirmed Day 4+ curriculum.

## Release gates
No real customer pilot without authorization, access controls, tested expiry/stock logic, secret management, manual fallback, audit and data retention policy. No autonomous medicine sales or purchasing.
