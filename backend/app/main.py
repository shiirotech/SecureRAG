from fastapi import FastAPI, UploadFile
from app.services.document_service import extract_text
from app.utils.text_splitter import split_text
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
    
    return {
        "filename": file.filename,
        "characters": len(text),
        "chunks": len(chunks)
    }