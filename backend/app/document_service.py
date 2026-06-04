import os
import uuid
import shutil
import json

UPLOAD_DIR = "uploads"
METADATA_FILE = "documents.json"

os.makedirs(UPLOAD_DIR, exist_ok=True)

if not os.path.exists(METADATA_FILE):
    with open(METADATA_FILE, "w") as f:
        json.dump([], f)


def upload_pdf(pdf_path,original_filename=None):
    if not os.path.exists(pdf_path):
        raise FileNotFoundError("PDF file not found")

    if not pdf_path.lower().endswith(".pdf"):
        raise ValueError("Only PDF files are allowed")

    document_id = str(uuid.uuid4())

    document_folder = os.path.join(
        UPLOAD_DIR,
        document_id
    )

    os.makedirs(document_folder, exist_ok=True)

    filename = os.path.basename(pdf_path)

    if original_filename:
        filename = original_filename

    destination_path = os.path.join(
        document_folder,
        filename
    )

    shutil.copy2(
        pdf_path,
        destination_path
    )

    document_data = {
        "document_id": document_id,
        "filename": filename,
        "path": destination_path,
        "status": "uploaded"
    }

    with open(METADATA_FILE, "r") as f:
        documents = json.load(f)

    documents.append(document_data)

    with open(METADATA_FILE, "w") as f:
        json.dump(documents, f, indent=4)

    return document_data





def view_document(document_id):
    with open(METADATA_FILE, "r") as f:
        documents = json.load(f)

    for doc in documents:
        if doc["document_id"] == document_id:
            return doc

    raise ValueError("Document not found")




def list_documents():
    with open(METADATA_FILE, "r") as f:
        return json.load(f)
