from backend.app.document_service import upload_pdf,view_document,list_documents
from backend.app.pdf_service import  extract_text,create_chunks
from backend.app.vector_store import create_vector_store,load_vector_store
from backend.app.generator import generate_answer
from backend.app.config import embedding_model
import json


def upload_workflow(pdf_path,original_filename=None):
    # pdf_path = input("Enter PDF path: ")
    try:
        result = upload_pdf(pdf_path, original_filename)
        text = extract_text(result["path"])
        chunks = create_chunks(text)
        create_vector_store(
            chunks,
            embedding_model,
            result["document_id"]
        )
        print("\nUploaded Successfully")
        print(json.dumps(result, indent=4))
        return result
    except Exception as e:
        print("Error:", e)


def chat_workflow(document_id, question):
    try:
        db = load_vector_store(
            embedding_model,
            document_id
        )

        answer = generate_answer(
            question,
            db
        )
        if isinstance(answer, str): 
            return answer
        return answer.content

    except Exception as e:
        return str(e)


def view_document_workflow(document_id, question):
    return chat_workflow(
        document_id,
        question
    )


def list_document_workflow():
    try:
        docs = list_documents()
        print("\nDocuments:")
        print(json.dumps(docs, indent=4))
        return docs
    except Exception as e:
        print("Error:", e)
        
def main():

    while True:

        print("\n===== PDF RAG System =====")
        print("1. Upload PDF")
        print("2. View Document & Chat")
        print("3. List Documents")
        print("4. Exit")
        choice = input("Enter Choice: ")
        if choice == "1":
            upload_workflow()
        elif choice == "2":
            view_document_workflow()
        elif choice == "3":
            list_document_workflow()
        elif choice == "4":
            print("Goodbye")
            break
        else:
            print("Invalid Choice")

if __name__ == "__main__":
    main()