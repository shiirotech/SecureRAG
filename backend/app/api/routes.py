from fastapi import APIRouter, UploadFile, HTTPException
from app.services.document_service import extract_text
from app.utils.text_splitter import split_text
from app.rag.embeddings import generate_embeddings
from app.rag.retrieval import store_embeddings
from app.rag.pipeline import run_rag_pipeline
import shutil
import os

router = APIRouter()

@router.get("/")
def root():
    return {"message": "SecureRAG backend running"}

@router.get("/documents")
async def get_documents():
    files = [
        file for file in os.listdir("documents")
        if file != ".gitkeep"
    ]

    return {
        "documents": files
    }

ALLOWED_TYPES = [".pdf", ".txt"]

@router.post("/upload")
async def upload_document(file: UploadFile):
    if not any(file.filename.lower().endswith(ext) for ext in ALLOWED_TYPES):
        raise HTTPException(status_code=400, detail="Invalid file type")
    
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

@router.post("/ask")
async def ask_question(question: str):
    answer, retrieved_chunks = run_rag_pipeline(question)

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