# injection_detector.py

# suspicious phrases commonly used in prompt injection / jailbreak attacks
SUSPICIOUS_PATTERNS = [
    "ignore previous instructions",
    "reveal system prompt",
    "bypass safety",
    "act as system",
    "developer mode",
    "jailbreak"
]

def injection_score(text):
    """
    Calculates a simple injection risk score.
    """

    score = 0
    text = text.lower()

    for pattern in SUSPICIOUS_PATTERNS:
        if pattern in text:
            score += 0.2

    # limit score to maximum 1.0
    return min(score, 1.0)