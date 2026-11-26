# Day 01 — How LLMs work and your first API call

## Objective
Adapt the faculty's Sweet Crumbs example to Medivora AI, a proposed pharmacy operations copilot. Explore next-token prediction, tokens, temperature, stateless calls, context windows, hallucinations and the first Groq API call. No live inventory is connected.

## Run
In Colab, open the notebook and add `GROQ_API_KEY` under Secrets, allowing notebook access. Run cells in order. Locally, install dependencies with `pip install -r requirements.txt` from the repository root, set the environment variable securely, then run `python Day-01/task.py`. Never publish keys or real pharmacy data.

Default model: `openai/gpt-oss-20b` (faculty HTML); the faculty notebook also uses `openai/gpt-oss-120b`. Set GROQ_MODEL to an available compatible model if needed. Model availability and temperature support depend on the provider. Prompt Guard is optional and uses the faculty notebook's model by default.

## Assignment mapping
- Five facts, three rules, and three business questions: system prompt and business demo.
- Temperature: three trials at 0.2 and three at 1.2; compare actual answers.
- Hallucination: compare grounded and ungrounded answers about same-day installation; ungrounded answers are not real company claims.
- Memory: separate calls versus explicitly supplied history.
- Tokens: compare actual English and Telugu prompt token counts.
- Prompt Guard: benign injection example, separate from chatbot.
- Ten questions for Day 02: below.

## Day 02 preparation — ten customer FAQs
1. What is Medivora AI?
2. Who is the intended customer?
3. Can it identify low-stock products?
4. Will it track expiry by batch?
5. Can it show current medicine availability?
6. Can it generate daily and monthly sales reports?
7. Can it suggest a reorder list?
8. Can it integrate with my existing billing system?
9. What is the subscription price?
10. Can staff use it without access to other stores' data?

These are prospective customer questions, not validated market research.

## Results
Implementation prepared; live API execution pending. Record actual responses and token counts after running with your key. No fabricated outputs or test pass claims. This is a learning prototype, not a clinical assistant or deployed pharmacy system.
