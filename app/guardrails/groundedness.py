from sentence_transformers import SentenceTransformer, util
from app.config import EMBED_MODEL, GROUNDEDNESS_THRESHOLD

model = SentenceTransformer(EMBED_MODEL)

def check_groundedness(answer, context_chunks):
    if not context_chunks:
        return 0.0, False
    answer_embedding = model.encode([answer])
    context_embeddings = model.encode(context_chunks)
    scores = util.cos_sim(answer_embedding, context_embeddings)
    max_score = float(scores.max())
    return max_score, max_score >= GROUNDEDNESS_THRESHOLD