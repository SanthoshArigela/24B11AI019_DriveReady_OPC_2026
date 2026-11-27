# Day 04 original evaluation — 2026-11-27

Source: student screenshot of Colab extended evaluation, not a complete raw CSV or trace. Original rubric: 8 PASS, 7 FAIL, 2 ERROR (RateLimitError), 8/17 = 47.06%. Among completed cases: 8/15 = 53.33%. No revised results yet.

| Case | Original status | Observation |
|---|---|---|
| Introduction | PASS | Prototype |
| Customer | FAIL | Equivalent pharmacy staff wording |
| Low stock | FAIL | Demo lookup described; planned alerts omitted |
| Expiry | PASS | Planned |
| Live stock | FAIL | Demo stock described; explicit limitation missing |
| Reports | PASS | Planned |
| Reorder | FAIL | Draft workflow described |
| Billing | PASS | Not confirmed |
| Pricing | PASS | Not confirmed |
| Isolation | FAIL | Unsupported isolation claim |
| Price B | PASS | 600 |
| Stock C | FAIL | Incorrect unknown product response |
| Unknown X | FAIL | No pricing information; keyword mismatch |
| Zero quantity | ERROR | RateLimitError |
| Missing date | PASS | Asked for date |
| Zero reorder quantity | PASS | Rejected |
| Combined lookup | ERROR | RateLimitError |

Revised rubric is not directly comparable. Original tool traces unavailable. Google Sheets 404 followed input Hi; no successful write evidenced.
