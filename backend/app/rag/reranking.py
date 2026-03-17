def rerank_chunks(question, chunks):
    scored = []

    for chunk in chunks:
        score = question.lower() in chunk["text"].lower()
        scored.append((score, chunk))

    scored.sort(reverse=True, key=lambda x: x[0])
    
    return [c for _, c in scored]