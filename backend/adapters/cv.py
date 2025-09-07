from typing import Tuple


def classify(image_bytes: bytes) -> Tuple[str, float]:
    """Deterministic mock classifier based on image size."""
    size = len(image_bytes)
    label = "healthy" if size % 2 == 0 else "disease"
    confidence = 0.9 if label == "healthy" else 0.6
    return label, confidence
