import google.generativeai as genai
from app.config import GEMINI_API_KEY, LLM_MODEL

genai.configure(api_key=GEMINI_API_KEY)

def generate_answer(question, context_chunks):
    context_text = "\n\n".join(context_chunks)
    prompt = f"Answer the question using only the context below. If the answer is not in the context, say you don't know.\n\nContext:\n{context_text}\n\nQuestion: {question}"

    model = genai.GenerativeModel(LLM_MODEL)
    response = model.generate_content(prompt)
    return response.text