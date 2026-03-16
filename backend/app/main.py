from fastapi import FastAPI, UploadFile
from app.services.document_service import extract_text
from app.utils.text_splitter import split_text
from app.rag.embeddings import generate_embeddings
from app.rag.retrieval import store_embeddings
from app.rag.retrieval import search_similar_chunks
import shutil

app = FastAPI()

@app.get("/")
def root():
    return {"message": "SecureRAG backend running"}

@app.post("/upload")
async def upload_document(file: UploadFile):
    path = f"documents/{file.filename}"

    with open(path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    text = extract_text(path)

    chunks = split_text(text)

    embeddings = generate_embeddings(chunks)

    store_embeddings(chunks, embeddings)

    return {
        "filename": file.filename,
        "chunks": len(chunks),
        "stored_vectors": len(embeddings)
    }

@app.post("/ask")
async def ask_question(question: str):
    query_embedding = generate_embeddings([question])

    results = search_similar_chunks(query_embedding)

    return {
        "question": question,
        "retrieved-chunks": results
    }