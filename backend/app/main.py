from fastapi import FastAPI, UploadFile
from app.services.document_service import extract_text
from app.utils.text_splitter import split_text
from app.rag.embeddings import generate_embeddings
from app.rag.retrieval import store_embeddings
from app.rag.retrieval import search_similar_chunks
from app.rag.retrieval import load_index
from app.rag.generation import generate_answer
import shutil

app = FastAPI()

load_index()

@app.get("/")
def root():
    return {"message": "SecureRAG backend running"}

@app.post("/upload")
async def upload_document(file: UploadFile):
    path = f"documents/{file.filename}"

    with open(path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    pages = extract_text(path)

    all_chunks = []
    metadata = []

    for page in pages:
        chunks = split_text(page["text"])

        for chunk in chunks:
            all_chunks.append(chunk)

            metadata.append({
                "text": chunk,
                "page": page["page"],
                "document": file.filename
            })

    embeddings = generate_embeddings(all_chunks)

    store_embeddings(metadata, embeddings)

    return {
        "filename": file.filename,
        "chunks": len(all_chunks),
        "stored_vectors": len(embeddings)
    }

@app.post("/ask")
async def ask_question(question: str):
    query_embedding = generate_embeddings([question])

    retrieved_chunks = search_similar_chunks(query_embedding)

    answer = generate_answer(question, retrieved_chunks)

    return {
        "question": question,
        "answer": answer,
        "sources": [
            {
                "document": c["document"],
                "page": c["page"]
            }
            for c in retrieved_chunks
        ]
    }