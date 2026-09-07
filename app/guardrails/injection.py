INJECTION_PATTERNS = [
    "ignore previous instructions",
    "ignore all prior",
    "disregard the system prompt",
    "you are now",
    "act as if",
    "reveal your instructions",
    "print your system prompt",
    "override your guidelines",
    "jailbreak",
]

def detect_injection(text):
    lowered = text.lower()
    for pattern in INJECTION_PATTERNS:
        if pattern in lowered:
            return True
    return False