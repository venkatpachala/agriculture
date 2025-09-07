import hashlib


def synthesize(text_te: str) -> str:
    """Return a mock URL based on hash of text."""
    digest = hashlib.sha1(text_te.encode()).hexdigest()[:10]
    return f"https://example.com/tts/{digest}.mp3"
