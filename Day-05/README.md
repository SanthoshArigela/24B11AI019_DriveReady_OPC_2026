# Day 05 — Memory and RAG

Faculty tutorial: ChromaDB, one fact per chunk, search_faq, InMemorySaver, separate thread IDs, fresh-thread evaluation, 80% target, Day 06 workflow. RAG Working explains indexing and query flows. Separate PDF notebook follows RAG-2.ipynb: PyMuPDF, OCR fallback, 500/100 chunking, normalized MiniLM embeddings, FAISS inner product, Groq. Upload the original faculty PDF locally; it is not redistributed here.

[Main Colab](https://colab.research.google.com/github/SanthoshArigela/24B11AI019_DriveReady_OPC_2026/blob/main/Day-05/Medivora_AI_Day_05.ipynb) | [PDF Colab](https://colab.research.google.com/github/SanthoshArigela/24B11AI019_DriveReady_OPC_2026/blob/main/Day-05/PDF_RAG_Demo.ipynb)

Run main notebook sequentially. It embeds the Day 04 snapshot and fixtures. 20 facts, 24 independent agent cases and 5 memory turns. Sign-off counts errors as failures. PDF evaluation separate. Actual results pending. Download CSVs and inspect traces. Keyword rubric is approximate; retrieval distance threshold 0.65 is provisional and not calibrated. Prompt grounding reduces but does not eliminate hallucinations. Memory is process-local, not authenticated isolation. Day 04 trusted approval path remains separate from chat. Day 05 uses model-selected tools, not Day 04 deterministic routing, so combined lookup is a regression test. No live inventory or purchases.

Day 04 runtime verified by user; exact V3 score not supplied.

## Day 05 baseline sign-off and V2
Faculty target met: agent 83.33%, memory 100%, PDF 100%, combined agent and memory 86.21%, overall 87.88%. Baseline CSVs archived in Day-05/results/baseline/. V2 targeted fixes committed; live retest and Day 05 Sheets evidence pending. See Day-05/EXPERIMENT_RESULTS.md.
