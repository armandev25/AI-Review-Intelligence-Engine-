# AI Review Intelligence Engine  
**Retrieval-Augmented Generation (RAG) System for Product Review Analysis**

[![Python](https://img.shields.io/badge/Python-3.x-blue)](https://www.python.org/)
![GenAI](https://img.shields.io/badge/GenAI-RAG-brightgreen)
![NLP](https://img.shields.io/badge/NLP-Embeddings-orange)
![FAISS](https://img.shields.io/badge/VectorDB-FAISS-lightgrey)
![FastAPI](https://img.shields.io/badge/API-FastAPI-teal)
![Streamlit](https://img.shields.io/badge/UI-Streamlit-red)
![Status](https://img.shields.io/badge/Status-Completed-success)

---

## Overview

This project implements an **AI-powered review intelligence system** that uses **Retrieval-Augmented Generation (RAG)** to answer product-related questions and compare products using real Amazon customer reviews.

Instead of relying solely on a language model, the system first retrieves **semantically relevant reviews** from a vector database and then uses a Large Language Model to generate **evidence-grounded answers**.

**Design Philosophy:** Evidence-first generation. The LLM is only used after relevant reviews are retrieved, preventing hallucinated answers.

---

## Problem Statement

E-commerce platforms contain massive volumes of customer reviews.  
Manually analyzing these reviews to understand product quality, common issues, and differences between similar products is time-consuming and inefficient.

Traditional sentiment analysis only labels reviews as positive or negative and does not support **question-driven product insights**.

This project addresses the need for a system that can:

- Retrieve relevant reviews for a user query  
- Generate concise, evidence-based answers  
- Support product-to-product comparison  

---

## Dataset

- **Source:** Amazon Reviews Dataset (US)
- **Domains Used:**
  - Mobile Electronics  
  - Personal Care Appliances  
  - Major Appliances  

**Fields Used**

- `product_title` → Product name  
- `review_body` → Review text  
- `star_rating` → Rating  

The dataset acts as a proxy for real-world e-commerce review data.

---

## System Workflow

1. Load and preprocess review data  
2. Generate embeddings for each review  
3. Store embeddings in FAISS vector database  
4. Convert user query into embedding  
5. Retrieve top-k relevant reviews  
6. Inject reviews into LLM prompt  
7. Generate grounded answer  

---

## Architecture

```text
User Query
   ↓
Embedding Model
   ↓
FAISS Vector Database (Semantic Search)
   ↓
Top Relevant Reviews
   ↓
Prompt Construction
   ↓
Large Language Model
   ↓
Grounded Answer / Comparison
```

---

## Core Components

### 1. Sentence Transformer Embeddings
- Model: `all-MiniLM-L6-v2`
- Converts reviews and queries into dense vectors

### 2. FAISS Vector Database
- Stores review embeddings
- Enables fast similarity search

### 3. Retriever
- Finds top-k relevant reviews for a query

### 4. LLM (via Groq API)
- Generates answers using retrieved context

### 5. Backend API
- FastAPI endpoints for asking questions and listing products

### 6. Frontend UI
- Streamlit web interface

---

## Supported Features

- Ask questions about a product  
- Extract strengths and weaknesses  
- Check product reliability  
- Compare two products  
- Discover available products  

---

## Example Queries
```text
- What do people like about this product?
- What are common complaints?
- Is this product reliable?
- Compare Product A and Product B
```

---

## Screenshots

### Ask Product Question
<img width="1919" height="862" alt="Screenshot 2026-02-01 175112" src="https://github.com/user-attachments/assets/f64f1b3e-7d41-4b38-9a44-62df5c04fa70" />
<img width="1919" height="864" alt="Screenshot 2026-02-01 175215" src="https://github.com/user-attachments/assets/6a11ec30-c046-4d03-8fe0-580a10cbe05f" />

### Compare Products
<img width="1919" height="864" alt="3" src="https://github.com/user-attachments/assets/01d6f33c-4e18-4c51-8704-7ba55040e17f" />
<img width="1919" height="397" alt="4" src="https://github.com/user-attachments/assets/e97da4b6-aa99-47e9-841d-6faf33c7321d" />

### Product Dropdown
<img width="1919" height="868" alt="5" src="https://github.com/user-attachments/assets/aaec1c48-606a-4701-9ae7-a2912b2d9ef6" />

---

## Tech Stack

- Python  
- Pandas, NumPy  
- Sentence-Transformers  
- FAISS  
- FastAPI  
- Streamlit  
- Groq LLM API  

---

## Limitations

- Static dataset snapshot  
- No real-time review scraping  
- No persistent chat memory  

---

## Future Improvements

- Upload custom review CSV  
- Product URL ingestion  
- Hybrid keyword + semantic search  
- Chat history  
- Cloud deployment  

---

## Conclusion

This project demonstrates how Retrieval-Augmented Generation can be applied to real-world product review analysis to generate **trustworthy, evidence-based insights** rather than hallucinated responses. It showcases an end-to-end GenAI system combining NLP, vector databases, and LLMs.

