import os
from dotenv import load_dotenv

load_dotenv()


# Base paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "..", "data", "processed")

# Dataset files
MOBILE_FILE = "../data/processed/mobile_electronics.csv"
PERSONAL_CARE_FILE = "../data/processed/personal_care.csv"
MAJOR_APPLIANCES_FILE = "../data/processed/major_appliances.csv"

# Embedding model
EMBEDDING_MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"

# Vector store path
FAISS_INDEX_PATH = os.path.join(BASE_DIR, "faiss_index")

# Hugging Face API
HF_API_KEY = os.getenv("HF_API_KEY")
LLM_MODEL_NAME = "HuggingFaceH4/zephyr-7b-beta"
