from app.core.chunker import chunk_text

sample = "A" * 50 + "B" * 50
result = chunk_text(sample, chunk_size=30, overlap=5)

for i, chunk in enumerate(result):
    print(f"Chunk {i}: {chunk}")