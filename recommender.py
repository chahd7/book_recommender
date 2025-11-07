# recommender.py

import pandas as pd
import faiss
import requests
import numpy as np


df = pd.read_csv("books_with_textual.csv")

index = faiss.read_index("vector_index.faiss")


def recommender(textual_representation):
    """Return the 5 most similar books given a textual representation."""
    res = requests.post("http://localhost:11434/api/embeddings",
                        json={
                            "model": "llama2",
                            "prompt": textual_representation
                        })
    embedding = np.array([res.json()["embedding"]], dtype="float32")
    D, I = index.search(embedding, 5)
    best_matches = df.iloc[I.flatten()]
    return best_matches


if __name__ == "__main__":
    sample_input = df.iloc[0]["textual_representation"]
    print(recommender(sample_input))
