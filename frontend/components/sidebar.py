import streamlit as st

from frontend.utils.api_client import api


def render_sidebar():

    with st.sidebar:

        st.title("🧠 Semantic Search Engine")

        st.caption(
            "Enterprise Multi-PDF RAG Assistant"
        )

        st.divider()

        st.subheader("Backend Status")

        try:

            status = api.health()

            st.success(status["status"])

        except Exception:

            st.error("Backend Offline")

        st.divider()

        st.subheader("Knowledge Base")

        try:

            docs = api.documents()

            st.metric(
                "Indexed PDFs",
                len(docs)
            )

            for document in docs:

                st.caption("📄 " + document)

        except Exception:

            st.warning("Unable to load documents.")

        st.divider()

        st.subheader("Conversation")

        if st.button("🗑 Clear Chat"):

            st.session_state.messages = []

            st.rerun()