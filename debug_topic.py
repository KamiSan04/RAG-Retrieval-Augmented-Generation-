from sentence_transformers import SentenceTransformer, util
from app.config import ALLOWED_TOPICS, EMBED_MODEL

model = SentenceTransformer(EMBED_MODEL)
topic_embeddings = model.encode(ALLOWED_TOPICS)

query = "How long do I have to return an item?"
query_embedding = model.encode([query])
scores = util.cos_sim(query_embedding, topic_embeddings)

for topic, score in zip(ALLOWED_TOPICS, scores[0]):
    print(topic, float(score))