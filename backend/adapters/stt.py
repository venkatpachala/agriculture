import base64


def transcribe(audio_b64: str) -> str:
    """Stub speech-to-text that ignores audio and returns fixed text."""
    try:
        base64.b64decode(audio_b64)
    except Exception:
        raise ValueError("Invalid base64 audio")
    return "stub transcript"
