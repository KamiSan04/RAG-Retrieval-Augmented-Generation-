import chromadb
from sentence_transformers import SentenceTransformer
from app.config import CHROMA_DIR, EMBED_MODEL, TOP_K

class VectorStore:
    def __init__(self):
        self.client = chromadb.PersistentClient(path=CHROMA_DIR)
        self.collection = self.client.get_or_create_collection("docs")
        self.embedder = SentenceTransformer(EMBED_MODEL)

    def add(self, chunks, metadatas, ids):
        embeddings = self.embedder.encode(chunks).tolist()
        self.collection.add(documents=chunks, embeddings=embeddings, metadatas=metadatas, ids=ids)

    def query(self, text, k=TOP_K):
        embedding = self.embedder.encode([text]).tolist()
        results = self.collection.query(query_embeddings=embedding, n_results=k)
        docs = results.get("documents", [[]])[0]
        metas = results.get("metadatas", [[]])[0]
        dists = results.get("distances", [[]])[0]
        return list(zip(docs, metas, dists))

store = VectorStore()