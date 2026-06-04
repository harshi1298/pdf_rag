import sys
import streamlit as st
import tempfile
import os


ROOT_DIR = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        ".."
    )
)


sys.path.append(ROOT_DIR)
from backend.app.main import upload_workflow, view_document_workflow, list_document_workflow


st.set_page_config(
    page_title="PDF RAG Assistant",
    layout="wide"
)


st.title("PDF RAG Assistant")


tab1, tab2, tab3 = st.tabs(
    [
        "Upload PDF",
        "Documents",
        "Chat"
    ]
)


with tab1:

    uploaded_file = st.file_uploader(
        "Upload PDF",
        type=["pdf"]
    )

    if uploaded_file:

        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".pdf"
        ) as tmp:

            tmp.write(uploaded_file.read())

            temp_path = tmp.name

        result = upload_workflow(temp_path, original_filename=uploaded_file.name)

        st.success("PDF Uploaded")

        st.json(result)



with tab2:

    docs = list_document_workflow()

    if docs:

        for doc in docs:

            st.write(
                f"📄 {doc['filename']}"
            )

            st.caption(
                f"ID: {doc['document_id']}"
            )

    else:

        st.info(
            "No documents uploaded"
        )


with tab3:

    docs = list_document_workflow()

    if docs and len(docs) == 0:

        st.warning(
            "Upload a PDF first"
        )

    else:

        selected_doc = st.selectbox(
            "Select Document",
            docs,
            format_func=lambda x: x["filename"]
        )

        question = st.text_input(
            "Ask a Question"
        )

        if st.button("Submit"):
            document_id = selected_doc["document_id"]
            answer =view_document_workflow(document_id,question)
            st.markdown("### Answer")

            st.write(answer)