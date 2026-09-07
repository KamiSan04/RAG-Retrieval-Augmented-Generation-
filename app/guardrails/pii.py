from presidio_analyzer import AnalyzerEngine
from presidio_anonymizer import AnonymizerEngine

analyzer = AnalyzerEngine()
anonymizer = AnonymizerEngine()

def redact_pii(text):
    results = analyzer.analyze(text=text, language="en")
    if not results:
        return text, False
    redacted = anonymizer.anonymize(text=text, analyzer_results=results)
    return redacted.text, True