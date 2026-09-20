import os
import sys
import streamlit as st

PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../..")
)

if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from frontend.utils.api_client import api

UPLOAD_DIRECTORY = os.path.join(PROJECT_ROOT, "uploads")

os.makedirs(UPLOAD_DIRECTORY, exist_ok=True)

st.set_page_config(page_title="Upload Documents")

st.title("📄 Upload PDF Documents")

st.caption("Upload PDFs into your Semantic Search Engine knowledge base.")

collection = st.selectbox(
    "Choose Collection",
    ["AI", "Finance", "Legal", "General"]
)

uploaded_files = st.file_uploader(
    "Upload one or more PDFs",
    type=["pdf"],
    accept_multiple_files=True
)

if uploaded_files:

    for file in uploaded_files:

        collection_path = os.path.join(
            UPLOAD_DIRECTORY,
            collection
        )

        os.makedirs(collection_path, exist_ok=True)

        file_path = os.path.join(
            collection_path,
            file.name
        )

        with open(file_path, "wb") as f:
            f.write(file.getbuffer())

        st.success(f"Saved: {file.name}")

        with st.spinner("Indexing document..."):

            response = api.index_document(
                filename=file_path
            )

        st.info(response["message"])

st.divider()

if st.button("Refresh Knowledge Base"):

    docs = api.documents()

    st.write(docs)