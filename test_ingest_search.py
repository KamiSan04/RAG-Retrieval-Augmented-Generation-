from app.core.vector_store import store

results = store.query("how many vacation days do employees get?")
for doc, meta, dist in results:
    print(doc, meta, dist)