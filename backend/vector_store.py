import faiss
import os
import numpy as np
from config import FAISS_INDEX_PATH


class VectorStore:
    def __init__(self, dim: int):
        """
        dim = embedding vector size (384 for MiniLM)
        """
        self.dim = dim
        self.index = faiss.IndexFlatL2(dim)

    def add_embeddings(self, embeddings):
        """
        embeddings: List or numpy array
        """
        vectors = np.array(embeddings).astype("float32")
        self.index.add(vectors)

    def save_index(self):
        os.makedirs(FAISS_INDEX_PATH, exist_ok=True)
        file_path = os.path.join(FAISS_INDEX_PATH, "reviews.index")
        faiss.write_index(self.index, file_path)
        print("FAISS index saved at:", file_path)

    def load_index(self):
        file_path = os.path.join(FAISS_INDEX_PATH, "reviews.index")
        if not os.path.exists(file_path):
            raise FileNotFoundError("FAISS index not found")
        self.index = faiss.read_index(file_path)
        print("FAISS index loaded")

    def search(self, query_vector, k=5):
        """
        query_vector: single embedding
        returns: distances, indices
        """
        query_vector = np.array([query_vector]).astype("float32")
        distances, indices = self.index.search(query_vector, k)
        return distances, indices


# Quick test
if __name__ == "__main__":
    from embedder import Embedder

    texts = [
        "Camera quality is excellent",
        "Battery drains quickly",
        "Great software experience",
        "Heats during gaming"
    ]

    embedder = Embedder()
    embeddings = embedder.generate_embeddings(texts)

    store = VectorStore(dim=len(embeddings[0]))
    store.add_embeddings(embeddings)
    store.save_index()

    store.load_index()

    query = "phone camera"
    q_vector = embedder.generate_embeddings([query])[0]
    distances, indices = store.search(q_vector)

    print("Search indices:", indices)
