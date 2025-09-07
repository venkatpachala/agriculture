import pickle
from pathlib import Path
import numpy as np
from .loader import load_docs
from .embed import embed_text

INDEX_PATH = Path(__file__).resolve().parent.parent / 'data' / 'index.pkl'

def build_index():
    docs = load_docs()
    embeddings = {k: embed_text(v) for k, v in docs.items()}
    with open(INDEX_PATH, 'wb') as f:
        pickle.dump({'docs': docs, 'embeddings': embeddings}, f)

if __name__ == '__main__':
    build_index()
    print('index built', INDEX_PATH)
