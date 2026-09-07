from app.guardrails.pii import redact_pii

sample = "Hi, my name is John Smith and my email is john.smith@example.com, call me at 555-123-4567."
clean_text, found = redact_pii(sample)

print("Found PII:", found)
print("Redacted:", clean_text)