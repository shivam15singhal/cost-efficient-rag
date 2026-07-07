# Cost-Efficient RAG Application

A Retrieval-Augmented Generation (RAG) application that provides grounded question answering over PDF, HTML, and Markdown documents using ChromaDB as a low-cost vector database and Google's Gemini API for answer generation.

---

## Features

- PDF, HTML and Markdown ingestion
- Configurable chunk size and overlap
- Idempotent re-ingestion (duplicate-safe)
- Semantic search using ChromaDB
- Metadata filtering
- Grounded responses with citations
- No-context fallback to prevent hallucination
- FastAPI REST API
- CLI interface
- Retrieval evaluation (Recall@k, MRR, nDCG, Context Precision)
- Latency measurement
- Cost comparison with managed vector databases

---

## Tech Stack

- Python 3.11
- LangChain
- ChromaDB
- BAAI/bge-small-en-v1.5
- Google Gemini API
- FastAPI
- Pydantic

---

## Folder Structure

```
cost-efficient-rag/
│
├── app/
├── scripts/
├── evaluation/
├── data/
├── chroma_db/
├── README.md
└── requirements.txt
```

---

## Installation

```bash
git clone <repository>

cd cost-efficient-rag

python -m venv .venv

.venv\Scripts\activate

pip install -r requirements.txt
```

---

## Environment Variables

```
GEMINI_API_KEY=
CHROMA_DB_PATH=
RAW_DATA_DIRECTORY=
CHUNK_SIZE=
CHUNK_OVERLAP=
TOP_K=
SIMILARITY_THRESHOLD=
```

---

## Ingest Documents

```bash
python -m scripts.ingest
```

---

## CLI

```bash
python -m scripts.ask
```

---

## REST API

```bash
python run.py
```

Swagger:

```
http://127.0.0.1:8000/docs
```

---

## Evaluation

```bash
python -m evaluation.evaluate
```

---

## Retrieval Results

- Recall@k = 1.00
- Hit Rate = 1.00
- MRR = 1.00
- nDCG = 1.00
- Context Precision = 0.592

Latency

- p50 = 28.75 ms
- p95 = 30.72 ms

---

## Cost Comparison

ChromaDB provides significantly lower infrastructure costs than managed vector databases for small-to-medium deployments while requiring self-managed hosting and backups.

---

## Design Decisions

- ChromaDB selected for low infrastructure cost.
- BAAI/bge-small-en-v1.5 selected for good quality-to-cost ratio.
- Metadata filtering added to support document-specific retrieval.
- Safe fallback prevents hallucinated answers when no relevant context is retrieved.

---

## Future Improvements

- Multi-document ranking
- Hybrid search
- Streaming responses
- Reranking
- Docker deployment