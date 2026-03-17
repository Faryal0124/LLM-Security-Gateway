# presidio_engine.py

from presidio_analyzer import AnalyzerEngine, PatternRecognizer, Pattern

# Initialize Presidio analyzer
analyzer = AnalyzerEngine()

# -------------------------------
# Custom Recognizer: API Key
# Example pattern: sk-123456789abcdef
# -------------------------------

api_key_pattern = Pattern(
    name="api_key_pattern",
    regex=r"sk-[A-Za-z0-9]{10,}",
    score=0.85
)

api_key_recognizer = PatternRecognizer(
    supported_entity="API_KEY",
    patterns=[api_key_pattern]
)

# Context-aware scoring words
api_key_recognizer.context = [
    "api",
    "token",
    "secret",
    "key",
    "apikey"
]

# Register the custom recognizer
analyzer.registry.add_recognizer(api_key_recognizer)


# -------------------------------
# Function to analyze text
# -------------------------------

def analyze_pii(text):
    """
    Detect PII entities using Presidio
    including custom recognizers
    """

    results = analyzer.analyze(
    text=text,
    language="en",
    entities=["PHONE_NUMBER", "EMAIL_ADDRESS", "API_KEY", "PERSON"]
)

    return results