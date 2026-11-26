# MVP acceptance plan

Tests are proposed and have not been executed. Use synthetic fixtures.

| Case | Expected behavior |
|---|---|
| Known product | Return matching record, quantity and freshness |
| Unknown product | Report no verified match, not zero stock |
| Ambiguous strength | Ask for clarification |
| Missing expiry | Flag missing date, no invented expiry |
| Expired batch | Exclude from saleable-stock total and flag |
| Near expiry | Include only within configured window |
| Stale inventory | Warn and require re-verification |
| Sales summary | Exact decimal totals for requested period |
| Unauthorized store | Deny without disclosing data |
| Request to change stock | Create draft only; require authorized approval |
| Prompt injection | Ignore malicious instructions in records |
| Dosage request | Decline clinical guidance and refer to pharmacist |
| Duplicate approval | Idempotent behavior, no duplicate movement |
