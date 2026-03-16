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


def search_similar_chunks(query_embedding, k = 3):
    global index, stored_chunks

    if index is None:
        return []
    
    distances, indices = index.search(query_embedding, k)

    results = []

    for idx in indices[0]:
        if idx < len(stored_chunks):
            results.append(stored_chunks[idx])

    return results