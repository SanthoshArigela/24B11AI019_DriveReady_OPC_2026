# Day 04 observed experiments

Original screenshot baseline: 8/17 PASS (47.06%), 7 FAIL, 2 ERROR. Revised uploaded agent CSV: 12/17 PASS (70.59%), 5 FAIL, 0 ERROR. Difference 23.53 percentage points; rubric changed, so not a controlled comparison.

Structured extraction: 5/5 exact JSON matches, all PASS. Naming trials: descriptive get_price (2 model calls), vague tool1 (2), restored get_price and is_available (3); all returned INR 600. Vague naming did not cause failure in this sample.

Remaining revised failures: low stock and live inventory wording mismatches; reorder answer suggested invalid high/medium/low priorities; store isolation answer began Yes despite admitting no isolation; combined lookup called get_price twice and reported unknown product. Unicode whitespace observed, but tool arguments unavailable, so cause not proven.

V3 introduces normalization, explicit priority constraints, revised approximate rubric and deterministic dual-tool routing for simple single-item price/stock questions. Routed calls are counted separately from LLM-selected calls (zero model calls). V3 live results pending. Google Sheets write evidence pending. No production inventory or purchase execution.
