import ollama

def generate_answer(question, context_chunks):
    context = "\n\n".join(c["text"] for c in context_chunks)

    prompt = f"""
You are an assistant answering questions about a document.

Only use the provided context to answer the question.
If the answer is not in the context, say you don't know.

Context:
{context}

Question:
{question}

Answer:
"""
    
    response = ollama.chat(
        model="mistral",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response["message"]["content"]