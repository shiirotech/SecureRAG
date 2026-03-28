import faiss
import numpy as np
import pickle
import os

INDEX_PATH = "vector_store/index.faiss"
CHUNKS_PATH = "vector_store/chunks.pkl"
index = None
stored_chunks = []

def save_index():
    global index, stored_chunks
    
    if index is not None:
        faiss.write_index(index, INDEX_PATH)

    with open(CHUNKS_PATH, "wb") as f:
        pickle.dump(stored_chunks, f)


def load_index():
    global index, stored_chunks

    if os.path.exists(INDEX_PATH):
        index = faiss.read_index(INDEX_PATH)
    
    if os.path.exists(CHUNKS_PATH):
        try:
            with open(CHUNKS_PATH, "rb") as f:
                stored_chunks = pickle.load(f)
        except EOFError:
            stored_chunks = []


def store_embeddings(metadata, embeddings):
    global index, stored_chunks

    embeddings = np.array(embeddings).astype("float32")
    dimension = embeddings.shape[1]

    if index is None:
        index = faiss.IndexFlatL2(dimension)
    
    index.add(embeddings)
    stored_chunks.extend(metadata)

    save_index()


def search_similar_chunks(query_embedding, k = 20):
    global index, stored_chunks

    if index is None:
        return []
    
    distances, indices = index.search(query_embedding, k)

    seen = set()
    results = []

    for idx in indices[0]:
        if idx < len(stored_chunks):
            chunk = stored_chunks[idx]["text"]

            if chunk not in seen:
                seen.add(chunk)
                results.append(stored_chunks[idx])

    return results