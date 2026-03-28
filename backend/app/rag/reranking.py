from sentence_transformers import CrossEncoder

reranker_model = CrossEncoder("BAAI/bge-reranker-base")

def rerank_chunks(question, chunks):
    if not chunks:
        return []
    
    pairs = [(question, chunk["text"]) for chunk in chunks]
    scores = reranker_model.predict(pairs)
    scored = list(zip(scores, chunks))
    scored.sort(reverse=True, key=lambda x: x[0])

    return [chunk for _, chunk in scored]