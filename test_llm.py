from app.core.llm import generate_answer

context = ["The refund policy allows returns within 30 days of purchase."]
answer = generate_answer("How long do I have to return an item?", context)
print(answer)