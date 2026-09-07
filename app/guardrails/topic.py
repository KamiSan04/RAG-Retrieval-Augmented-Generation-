from sentence_transformers import SentenceTransformer, util
from app.config import ALLOWED_TOPICS, EMBED_MODEL

model = SentenceTransformer(EMBED_MODEL)
topic_embeddings = model.encode(ALLOWED_TOPICS)

def is_on_topic(query, threshold=0.3):
    query_embedding = model.encode([query])
    scores = util.cos_sim(query_embedding, topic_embeddings)
    return float(scores.max()) >= threshold