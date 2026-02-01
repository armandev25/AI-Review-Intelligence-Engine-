from sentence_transformers import SentenceTransformer
from config import EMBEDDING_MODEL_NAME


class Embedder:
    def __init__(self):
        print("Loading embedding model...")
        self.model = SentenceTransformer(EMBEDDING_MODEL_NAME)

    def generate_embeddings(self, texts):
        """
        texts: List[str]
        returns: List of vectors
        """
        embeddings = self.model.encode(
            texts,
            show_progress_bar=True
        )
        return embeddings


# Quick test
if __name__ == "__main__":
    embedder = Embedder()
    sample_texts = [
        "Camera quality is excellent",
        "Battery drains quickly"
    ]
    vectors = embedder.generate_embeddings(sample_texts)
    print("Number of embeddings:", len(vectors))
    print("Vector size:", len(vectors[0]))
