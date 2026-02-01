from retriever import Retriever
from llm_client import LLMClient


class RAGPipeline:
    def __init__(self):
        self.retriever = Retriever()
        self.llm = LLMClient()

    def build_prompt(self, question, reviews):
        context = ""
        for r in reviews:
            context += f"- {r['review_text']} (Rating: {r['rating']})\n"

        prompt = f"""
You are an AI assistant that answers questions based ONLY on the reviews below.

Reviews:
{context}

Question:
{question}

Give a clear and helpful answer.
"""
        return prompt

    def ask(self, question):
        reviews = self.retriever.retrieve(question)
        prompt = self.build_prompt(question, reviews)
        answer = self.llm.generate(prompt)
        return answer


# Quick test
if __name__ == "__main__":
    rag = RAGPipeline()
    response = rag.ask("Is this phone good for gaming?")
    print(response)
