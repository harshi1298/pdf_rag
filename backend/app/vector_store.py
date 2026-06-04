from langchain_community.vectorstores import FAISS
import os

def create_vector_store(chunks, embedding_model,document_id):

    db = FAISS.from_texts(
        texts=chunks,
        embedding=embedding_model
    )
    
    index_path = os.path.join(
        "uploads",
        document_id,
        "faiss_index"
    )
    
    db.save_local(index_path)

    return db

def load_vector_store(embedding_model, document_id):
    index_path = os.path.join(
        "uploads",
        document_id,
        "faiss_index"
    )
    return FAISS.load_local(
        index_path,
        embedding_model,
        allow_dangerous_deserialization=True
    )