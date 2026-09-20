import os
import sys
import streamlit as st

PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../..")
)

if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from frontend.utils.api_client import api

st.title("📚 Knowledge Base Explorer")

st.caption("View every indexed document inside collections.")

collections = [
    "AI",
    "Finance",
    "Legal",
    "General"
]

selected = st.selectbox(
    "Collection",
    collections
)

st.divider()

docs = api.documents()

for doc in docs:

    st.container(border=True)

    st.markdown(f"### 📄 {doc}")

    st.caption(selected)

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Chunks", "20")

    with col2:
        st.metric("Status", "Indexed")