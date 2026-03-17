import ollama

def generate_answer(question, context_chunks):
    context = "\n\n".join(c["text"] for c in context_chunks)

    prompt = f"""
You are a technical assistant working with a scientific document.

Answer using ONLY the provided context.

IMPORTANT:
- Do NOT give a high-level summary
- Provide a detailed, mechanism-level explanation
- Use step-by-step reasoning when applicable
- Explicitly compare concepts if asked
- Use multiple parts of the context if relevant
- If information is missing, clearly state what is missing
- Do NOT invent information

Structure your answer clearly, but do not force unnecessary sections.

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