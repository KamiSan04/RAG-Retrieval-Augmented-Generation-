import os

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "")
CHROMA_DIR = "./data/chroma"
EMBED_MODEL = "all-MiniLM-L6-v2"
LLM_MODEL = "gemini-flash-latest"
TOP_K = 5
ALLOWED_TOPICS = [
    "questions about company policies, refunds, and returns",
    "questions about product documentation and how things work",
    "questions about engineering and technical topics",
    "questions about HR, employee benefits, and leave",
    "questions about finance, invoices, and payments",
]
GROUNDEDNESS_THRESHOLD = 0.55