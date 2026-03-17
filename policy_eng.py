# policy_eng.py

from presidio_anonymizer import AnonymizerEngine

anonymizer = AnonymizerEngine()

INJECTION_THRESHOLD = 0.4


def policy_decision(injection_score, pii_entities, text):

    if injection_score >= INJECTION_THRESHOLD:
        return "BLOCK", text

    if len(pii_entities) > 0:
        result = anonymizer.anonymize(
            text=text,
            analyzer_results=pii_entities
        )
        return "MASK", result.text

    return "ALLOW", text