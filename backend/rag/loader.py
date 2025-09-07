"""Load documents from data/docs"""
import os
from pathlib import Path

def load_docs(data_path: str | None = None) -> dict:
    data_path = data_path or Path(__file__).resolve().parent.parent / "data" / "docs"
    docs = {}
    for p in Path(data_path).glob("*.md"):
        docs[p.stem] = p.read_text(encoding="utf-8")
    return docs

if __name__ == "__main__":
    for k in load_docs().keys():
        print(k)
