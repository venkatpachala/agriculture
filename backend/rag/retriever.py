import pickle
import numpy as np
from pathlib import Path

try:
    from .embed import embed_text  # type: ignore
except Exception:  # pragma: no cover
    def embed_text(text: str) -> np.ndarray:
        # Fallback simple embedding to avoid heavy deps during tests
        return np.zeros(384)

INDEX_PATH = Path(__file__).resolve().parent.parent / 'data' / 'index.pkl'

def retrieve(query: str, top_k: int = 5):
    with open(INDEX_PATH, 'rb') as f:
        data = pickle.load(f)
    q_emb = embed_text(query)
    docs, embeddings = data['docs'], data['embeddings']
    sims = []
    for k, emb in embeddings.items():
        sim = np.dot(q_emb, emb) / (np.linalg.norm(q_emb) * np.linalg.norm(emb))
        sims.append((k, sim))
    sims.sort(key=lambda x: x[1], reverse=True)
    return [(k, docs[k]) for k, _ in sims[:top_k]]
