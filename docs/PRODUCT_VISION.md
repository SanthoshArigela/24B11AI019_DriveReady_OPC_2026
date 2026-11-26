# Product vision

## Customer problem
Independent pharmacies may use disconnected records for inventory, sales, purchases and expiry monitoring. Validate these issues with 5–10 owners and pharmacists before committing to product scope.

## Users
Owner/admin: reporting, configuration, staff management and approval. Pharmacist/manager: inventory queries, expiry review and permitted operational actions. Staff: limited lookup and draft requests.

## MVP
One read-first workflow: staff question → structured intent → validated authorized data lookup → deterministic computation → evidence-backed answer → optional action draft → authorized approval → audit.

Capabilities: product and batch lookup, low-stock thresholds, near-expiry list, expired stock flag, sales totals and draft reorder list. Show record IDs, last update and data-quality warnings. Never mark missing stock as zero or treat expired stock as saleable. Define expiry precision and cutoffs with the pilot pharmacist.

## Future modules
Invoice OCR with review; demand forecasting with backtesting; supplier comparison; multi-store reporting; integrations with existing billing systems. Do not implement autonomous purchases initially.

## Non-goals
Diagnosis, dosage recommendations, prescriptions, therapeutic substitutions, patient profiling, automated dispensing or authorization of restricted drug sales. No real data until authorization and security gates are met.

## Pilot success measures
Measure inventory lookup time, alert precision/recall against manually verified records, source-backed answer accuracy, staff acceptance, reporting time and API cost per query. Proposed goals: zero unsupported stock claims in acceptance tests, all write actions approved, and improved lookup time compared with baseline. No performance results are claimed.
