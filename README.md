# Semantic Search Engine — Enterprise Multi-PDF RAG Assistant

> A production-style Retrieval-Augmented Generation (RAG) system built from scratch in Python with semantic search, hybrid retrieval, reranking, conversational memory, context compression, citations, knowledge base management, and a FastAPI backend.

![Python](https://img.shields.io/badge/Python-3.13-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![FAISS](https://img.shields.io/badge/FAISS-Vector%20Search-orange)
![Sentence Transformers](https://img.shields.io/badge/SentenceTransformers-Embeddings-red)
![Pytest](https://img.shields.io/badge/Tests-36%20Passing-success)
![License](https://img.shields.io/badge/License-MIT-black)

---

## Project Overview

This project is a complete semantic search and Retrieval-Augmented Generation engine inspired by enterprise AI assistants such as ChatGPT, Perplexity AI, Claude Projects, Google NotebookLM, and internal company knowledge assistants.

Instead of calling an LLM directly, the engine retrieves relevant knowledge from documents, reranks results, compresses context, manages conversation memory, and prepares optimized prompts for any LLM.

The architecture is modular so components can be replaced independently.

---

## What This Project Can Do

* Search across multiple documents using embeddings.
* Perform vector search using FAISS.
* Perform keyword search using BM25.
* Combine retrieval methods using Hybrid Retrieval.
* Expand user queries automatically.
* Perform Multi-Query Retrieval.
* Fuse retrieval rankings using Reciprocal Rank Fusion (RRF).
* Rerank retrieved chunks using CrossEncoder.
* Build optimized context for LLMs.
* Compress context using semantic sentence scoring.
* Manage token budgets automatically.
* Store and retrieve conversational memory.
* Persist knowledge base metadata.
* Generate citations.
* Serve everything through a FastAPI REST API.

---

# Architecture

```text
                   User Question
                         │
                         ▼
                Query Expansion
                         │
        ┌────────────────┴─────────────────┐
        ▼                                  ▼
     BM25 Search                    FAISS Vector Search
        │                                  │
        └──────────────┬───────────────────┘
                       ▼
            Reciprocal Rank Fusion
                       ▼
           CrossEncoder Reranker
                       ▼
             Retrieved Chunks
                       ▼
      Conversation Memory Retriever
                       ▼
            Context Fusion Engine
                       ▼
         Compression Pipeline
                       ▼
          Prompt Builder + History
                       ▼
                 LLM Provider
                       ▼
          Answer + Citations + Memory
```

---

# Repository Structure

```text
semantic-search-engine/

├── api/
├── app/
├── citation/
├── context/
├── embeddings/
├── examples/
├── knowledge_base/
├── llm/
├── memory/
├── models/
├── reranking/
├── retrieval/
├── storage/
├── tests/
├── utils/
├── main.py
├── requirements.txt
└── README.md
```

---

# Features Implemented

## Phase 1 — Semantic Search Foundation

* PDF ingestion
* Recursive chunking
* Document models
* SentenceTransformer embeddings
* FAISS vector store
* Cosine similarity search

## Phase 2 — Retrieval Systems

* BM25 Retriever
* FAISS Retriever
* Hybrid Retrieval
* Reciprocal Rank Fusion
* Retrieval Evaluation Metrics
* Recall@K
* HitRate
* MRR
* NDCG

## Phase 3 — Intelligent Retrieval

* Query Expansion
* Multi Query Retrieval
* Hybrid Multi Query Retrieval
* Retrieval Benchmarking

## Phase 4 — Reranking

* CrossEncoder Reranker
* Hybrid + CrossEncoder Pipeline
* Production reranking examples

## Phase 5 — Context Engineering

* Context Builder
* Token Budget Manager
* Prompt Builder
* Citation Builder
* Streaming Responses

## Phase 6 — Conversational Memory

* Conversation Memory
* Persistent Memory Records
* Memory Vector Store
* Memory Manager
* Memory Retrieval
* Memory Ranking
* Metadata Filtering
* Threshold Filtering
* Memory Compression

## Phase 7 — Context Compression

* Sentence Similarity Scoring
* Extractive Compression
* Adaptive Compression
* Compression Pipeline
* Context Fusion Engine
* Token Allocation

## Phase 8 — Knowledge Base Management

* Knowledge Registry
* Collection Manager
* Batch PDF Indexing
* Incremental Indexing
* SHA256 Duplicate Detection
* Persistent Registry Storage

## Phase 9 — LLM Abstraction Layer

* Base LLM Interface
* Mock LLM
* Gemini Integration
* OpenAI Integration
* Provider-independent RAG Engine

## Phase 10 — FastAPI Backend

* `/health`
* `/chat`
* `/search`
* `/documents`
* `/index`
* OpenAPI documentation

---

# Tech Stack

| Layer         | Technology           |
| ------------- | -------------------- |
| Language      | Python 3.13          |
| Backend       | FastAPI              |
| Vector Search | FAISS                |
| Embeddings    | SentenceTransformers |
| Reranking     | CrossEncoder         |
| Testing       | Pytest               |
| Validation    | Pydantic v2          |
| API Docs      | Swagger UI           |

---

# Installation

```bash
git clone https://github.com/CREATORRADHEY/Semantic_search_Engine.git

cd Semantic_search_Engine

python3 -m venv .venv

source .venv/bin/activate

pip install -r requirements.txt
```

---

# Run the API

```bash
uvicorn main:app --reload
```

Open:

```
http://127.0.0.1:8000/docs
```

Swagger UI provides interactive API documentation.

---

# Running Examples

### Semantic Search

```bash
python3 -m examples.semantic_search_example
```

### Hybrid Retrieval

```bash
python3 -m examples.hybrid_retrieval_example
```

### Query Expansion

```bash
python3 -m examples.query_expansion_example
```

### Multi Query Retrieval

```bash
python3 -m examples.multi_query_example
```

### CrossEncoder Reranking

```bash
python3 -m examples.cross_encoder_example
```

### Context Builder

```bash
python3 -m examples.context_builder_example
```

### Conversation Memory

```bash
python3 -m examples.conversation_memory_example
```

### Memory Retrieval

```bash
python3 -m examples.memory_retriever_example
```

### Context Compression

```bash
python3 -m examples.adaptive_compression_example
```

### Knowledge Base

```bash
python3 -m examples.knowledge_base_example
```

---

# API Endpoints

| Endpoint         | Description              |
| ---------------- | ------------------------ |
| GET `/health`    | API health check         |
| POST `/chat`     | Chat with RAG assistant  |
| POST `/search`   | Retrieve relevant chunks |
| GET `/documents` | List indexed documents   |
| POST `/index`    | Index new document       |

---

# Testing

Run the full suite.

```bash
python3 -m pytest
```

Current Status:

```text
36 Passed
0 Failed
100% Passing
```

---

# Sample Retrieval Flow

1. User asks a question.
2. Query expansion generates alternatives.
3. BM25 and FAISS retrieve candidates.
4. Reciprocal Rank Fusion merges rankings.
5. CrossEncoder reranks results.
6. Conversation memory retrieves relevant past interactions.
7. Context Fusion merges memories and documents.
8. Compression Pipeline trims context.
9. Prompt Builder constructs LLM prompt.
10. LLM generates answer.
11. Citations are attached.
12. Memory is stored.

---

# Example Response

```json
{
  "answer": "FAISS is a vector similarity search library developed by Meta for efficient nearest-neighbor search.",
  "citations": [
    {
      "source": "faiss.pdf",
      "chunk_id": "chunk_12"
    }
  ]
}
```

---

# Engineering Highlights

### Retrieval Quality

* Hybrid Search
* Multi Query Retrieval
* Reciprocal Rank Fusion
* CrossEncoder Reranking

### Memory

* Persistent semantic memory.
* Metadata filtering.
* Similarity thresholding.
* Vector-based recall.

### Context Optimization

* Sentence scoring.
* Extractive summarization.
* Adaptive compression.
* Token budgeting.

### Knowledge Base

* Duplicate detection using SHA256.
* Incremental indexing.
* Batch indexing.
* Collection namespaces.

---

# Future Roadmap (Version 2.0)

## Agentic RAG

* Tool Calling
* Function Calling
* Planner + Executor Agents
* Reflection Loop

## Production Retrieval

* ChromaDB
* Pinecone
* Weaviate
* Milvus
* Elasticsearch Hybrid Search

## Enterprise Features

* Multi-user memory.
* Authentication.
* Role-based document access.
* Streaming APIs.
* Background indexing.

## Frontend

* React + Tailwind.
* Drag-and-drop PDF upload.
* ChatGPT-like interface.
* Streaming responses.
* Conversation history.

## Deployment

* Docker.
* Docker Compose.
* GitHub Actions CI/CD.
* AWS EC2 Deployment.
* GCP Cloud Run Deployment.

---

# Learning Goals Covered

This repository teaches production AI engineering concepts including:

* Embeddings
* Vector Databases
* Retrieval-Augmented Generation
* Hybrid Search
* CrossEncoder Reranking
* Context Engineering
* Conversation Memory
* Token Optimization
* FastAPI Backend Development
* Software Testing
* Modular AI System Design

---

# Project Status

| Module                  | Status |
| ----------------------- | ------ |
| Semantic Search         | ✅      |
| Hybrid Retrieval        | ✅      |
| Query Expansion         | ✅      |
| Multi Query Retrieval   | ✅      |
| CrossEncoder Reranking  | ✅      |
| Context Builder         | ✅      |
| Token Budget Manager    | ✅      |
| Prompt Builder          | ✅      |
| Conversation Memory     | ✅      |
| Memory Vector Store     | ✅      |
| Context Compression     | ✅      |
| Knowledge Base Registry | ✅      |
| Incremental Indexing    | ✅      |
| FastAPI Backend         | ✅      |
| Test Suite              | ✅      |

**Current Version:** `v1.0.0`

---

# About This Project

Built from scratch as part of a deep AI Engineering learning journey focused on production-ready Retrieval-Augmented Generation systems, scalable semantic search infrastructure, and enterprise AI assistant architecture.

**Author:** Divyansh Dusad

**Goal:** Build AI infrastructure before building AI applications.

