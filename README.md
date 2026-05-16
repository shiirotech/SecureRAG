# 🛡️ SecureRAG

A fully local Retrieval-Augmented Generation (RAG) assistant for secure interaction with private documents.

SecureRAG allows users to upload PDF/TXT files, retrieve semantically relevant context using vector search and reranking, and generate AI-powered answers using a local LLM via Ollama.

Built with a decoupled architecture using React frontend and FastAPI/Python backend.

---

# 🚀 Features

- Local AI inference with Ollama
- PDF/TXT document upload
- Semantic retrieval with FAISS
- Context reranking pipeline
- Source-aware AI responses
- Markdown-rendered answers
- Responsive chat interface
- Dockerized deployment support

---

# 🏗️ Tech Stack

## Frontend
- React
- JavaScript
- CSS

## Backend
- Python
- FastAPI
- Uvicorn

## AI / RAG
- Ollama
- Mistral
- Sentence Transformers
- FAISS

## DevOps
- Docker
- Docker Compose

---

# 🧠 Architecture

```text
User Question
↓
Embedding Generation
↓
FAISS Retrieval
↓
Reranking
↓
LLM Context Injection
↓
Local Response Generation
```

The system operates fully locally:
- documents stay on-device,
- embeddings are generated locally,
- vector search is local,
- LLM inference is local.

No cloud AI APIs are required.

---

# ⚙️ Running The Project

## 1. Clone the repository

```bash
git clone https://github.com/shiirotech/SecureRAG.git
cd SecureRAG
```

---

# 🚀 Option A — Native Setup

## Backend

```bash
cd backend

python -m venv venv
```

### Activate virtual environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux/macOS

```bash
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run backend

```bash
uvicorn app.main:app --reload
```

---

## Frontend

```bash
cd frontend

npm install
npm start
```

---

## Ollama

Install Ollama:

https://ollama.com

Pull and run the model:

```bash
ollama pull mistral
ollama serve
```

---

# 🐳 Option B — Docker Setup

Make sure Docker Desktop and Ollama are running.

Run from project root:

```bash
docker compose up --build
```

---

# 🎯 Motivation

I built this project in order to explore modern AI application architecture while preserving full local execution and document privacy.