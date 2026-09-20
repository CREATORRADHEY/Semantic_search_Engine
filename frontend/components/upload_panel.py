import os
import streamlit as st
from frontend.utils.api_client import api

UPLOAD_FOLDER = "uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def render_upload_panel():

    st.subheader("📤 Upload PDF")

    uploaded_file = st.file_uploader(
        "Drag & Drop PDF",
        type=["pdf"]
    )

    if uploaded_file is None:
        return

    save_path = os.path.join(
        UPLOAD_FOLDER,
        uploaded_file.name
    )

    with open(save_path, "wb") as file:
        file.write(uploaded_file.getbuffer())

    st.success(f"{uploaded_file.name} uploaded.")

    if st.button("⚡ Index PDF"):

        with st.spinner("Indexing..."):

            api.index_document(uploaded_file.name)

        st.success("Indexed Successfully!")

        st.rerun()