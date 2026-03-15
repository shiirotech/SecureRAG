import faiss
import numpy as np

index = None
stored_chunks = []

def store_embeddings(chunks, embeddings):
    global index, stored_chunks

    embeddings = np.array(embeddings).astype("float32")

    dimension = embeddings.shape[1]

    if index is None:
        index = faiss.IndexFlatL2(dimension)
    
    index.add(embeddings)

    stored_chunks.extend(chunks)