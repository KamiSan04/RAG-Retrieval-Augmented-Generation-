from fastapi import FastAPI
from pydantic import BaseModel
from app.guardrails.injection import detect_injection
from app.guardrails.topic import is_on_topic
from app.guardrails.pii import redact_pii
from app.guardrails.groundedness import check_groundedness
from app.core.vector_store import store
from app.core.llm import generate_answer

app = FastAPI()

class Question(BaseModel):
    question: str

@app.post("/ask")
def ask(payload: Question):
    question = payload.question

    if detect_injection(question):
        return {"error": "This question was blocked for containing a prompt injection attempt."}

    if not is_on_topic(question):
        return {"error": "This question is outside the allowed topics for this assistant."}

    clean_question, pii_found = redact_pii(question)

    results = store.query(clean_question)
    context_chunks = [doc for doc, meta, dist in results]

    if not context_chunks:
        return {"error": "No relevant documents found to answer this question."}

    answer = generate_answer(clean_question, context_chunks)

    score, grounded = check_groundedness(answer, context_chunks)

    return {
        "answer": answer,
        "grounded": grounded,
        "groundedness_score": score,
        "pii_redacted": pii_found,
        "sources": [meta["source"] for doc, meta, dist in results]
    }