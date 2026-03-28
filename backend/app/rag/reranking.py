from sentence_transformers import CrossEncoder

reranker_model = CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2")

def rerank_chunks(question, chunks):
    if not chunks:
        return []
    
    pairs = [(question, chunk["text"]) for chunk in chunks]
    scores = reranker_model.predict(pairs)
    scored = list(zip(scores, chunks))
    scored.sort(reverse=True, key=lambda x: x[0])

    return [chunk for _, chunk in scored]