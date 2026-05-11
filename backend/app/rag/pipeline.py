from app.rag.embeddings import generate_embeddings
from app.rag.retrieval import search_similar_chunks
from app.rag.generation import generate_answer
from app.rag.reranking import rerank_chunks

def run_rag_pipeline(question: str):
    query_embedding = generate_embeddings([question])

    retrieved_chunks = search_similar_chunks(query_embedding)

    retrieved_chunks = rerank_chunks(question, retrieved_chunks)

    retrieved_chunks = retrieved_chunks[:3]

    answer = generate_answer(question, retrieved_chunks)

    return answer, retrieved_chunks