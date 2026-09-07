from app.core.vector_store import store

chunks = ["The refund policy allows returns within 30 days.", "Our office is open 9am to 5pm on weekdays."]
metadatas = [{"source": "policy.txt"}, {"source": "hours.txt"}]
ids = ["chunk1", "chunk2"]

store.add(chunks, metadatas, ids)

results = store.query("how many days do I have to return something?")
for doc, meta, dist in results:
    print(doc, meta, dist)