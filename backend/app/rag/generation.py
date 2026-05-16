import ollama
import os

OLLAMA_HOST = os.getenv(
        "OLLAMA_HOST",
        "http://localhost:11434"
    )

client = ollama.Client(
    host=OLLAMA_HOST
)

def generate_answer(question, context_chunks):
    context = ""
    for i, c in enumerate(context_chunks):
        context += f"""
    Source: {c['document']}
    Page: {c['page']}
    Content:
    {c['text']}
    """

    prompt = f"""
    You are answering questions about a scientific paper.

    Use ONLY the provided excerpts.

    Requirements:
    - Use Markdown formatting
    - Base every claim on the provided excerpts
    - Prefer precise mechanism-level explanations
    - Avoid vague summaries
    - If multiple excerpts discuss the same concept, synthesize them carefully
    - Do not reference excerpts using labels like CHUNK or EXCERPT in the answer.
    - Do not repeat the same idea unnecessarily
    - If the context is insufficient, explicitly say so

    Relevant excerpts:

    {context}

    Question:
    {question}

    Answer:
    """

    response = client.chat(
        model="mistral",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response["message"]["content"]