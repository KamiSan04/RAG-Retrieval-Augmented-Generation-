import sys
import os
from pypdf import PdfReader
from app.core.chunker import chunk_text
from app.core.vector_store import store

def load_text_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def load_pdf_file(path):
    reader = PdfReader(path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text

def ingest(path):
    filename = os.path.basename(path)
    if path.lower().endswith(".pdf"):
        text = load_pdf_file(path)
    else:
        text = load_text_file(path)

    chunks = chunk_text(text)
    ids = [f"{filename}_{i}" for i in range(len(chunks))]
    metadatas = [{"source": filename} for _ in chunks]

    store.add(chunks, metadatas, ids)
    print(f"Ingested {len(chunks)} chunks from {filename}")

if __name__ == "__main__":
    file_path = sys.argv[1]
    ingest(file_path)