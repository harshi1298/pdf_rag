from langchain_huggingface import HuggingFaceEmbeddings

UPLOAD_DIR = "uploads"
METADATA_FILE = "documents.json"

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)