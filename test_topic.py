from app.guardrails.topic import is_on_topic

on_topic_q = "What is the company's refund policy?"
off_topic_q = "Write me a poem about cats."

print("On-topic question allowed:", is_on_topic(on_topic_q))
print("Off-topic question allowed:", is_on_topic(off_topic_q))