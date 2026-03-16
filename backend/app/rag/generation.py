import ollama

def generate_answer(question, context_chunks):
    context = "\n\n".join(context_chunks)

    prompt = f"""
Use the following document context to answer the question.

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