from data_loader import load_dataset
from embedder import Embedder
from vector_store import VectorStore


class Retriever:
    def __init__(self):
        # Load dataset
        self.data = load_dataset()

        # Load embedding model
        self.embedder = Embedder()

        # Create vector store and load existing FAISS index
        sample_embedding = [0.0] * 384
        self.store = VectorStore(dim=len(sample_embedding))
        self.store.load_index()

    def retrieve(self, query, k=5):
        """
        Retrieve top-k relevant reviews for a query
        """
        query_vector = self.embedder.generate_embeddings([query])[0]
        distances, indices = self.store.search(query_vector, k)

        results = []
        for idx in indices[0]:
            if idx == -1:
                continue

            row = self.data.iloc[idx]
            results.append({
                "item_name": row["item_name"],
                "review_text": row["review_text"],
                "rating": row["rating"]
            })

        return results

    def list_products(self, limit=20):
        """
        Return most frequent product names
        """
        products = self.data["item_name"].value_counts().head(limit)
        return list(products.index)


# Quick test
if __name__ == "__main__":
    retriever = Retriever()

    print("Top products:")
    for p in retriever.list_products():
        print(p)

    print("\nSample retrieval:")
    results = retriever.retrieve("good camera")

    for r in results:
        print(r)
