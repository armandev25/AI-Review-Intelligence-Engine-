from fastapi import FastAPI
from pydantic import BaseModel
from rag_pipeline import RAGPipeline

app = FastAPI()
rag = RAGPipeline()


class QueryRequest(BaseModel):
    question: str


@app.get("/")
def home():
    return {"message": "AI Review Intelligence Engine is running"}


@app.post("/ask")
def ask_question(req: QueryRequest):
    answer = rag.ask(req.question)
    return {"answer": answer}


@app.get("/products")
def get_products():
    products = rag.retriever.list_products()
    return {"products": products}
