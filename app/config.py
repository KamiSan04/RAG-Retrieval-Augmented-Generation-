import os

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "")
CHROMA_DIR = "./data/chroma"
EMBED_MODEL = "all-MiniLM-L6-v2"
LLM_MODEL = "gemini-1.5-flash"
TOP_K = 5
ALLOWED_TOPICS = ["company policy", "product docs", "engineering", "hr", "finance"]
GROUNDEDNESS_THRESHOLD = 0.55