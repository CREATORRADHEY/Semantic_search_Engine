import os
import sys
import streamlit as st

PROJECT_ROOT = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        ".."
    )
)

if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from frontend.utils.api_client import api

from frontend.components.sidebar import render_sidebar

from frontend.components.chat_window import (
    initialize_chat,
    display_messages,
    add_user_message,
    add_assistant_message
)

from frontend.components.streaming import (
    stream_generator
)

st.set_page_config(
    page_title="Semantic Search Engine",
    page_icon="🤖",
    layout="wide"
)

render_sidebar()

initialize_chat()

st.title("🤖 Enterprise Semantic Search Assistant")

st.caption(
    "Hybrid RAG + Memory Retrieval + Streaming Responses"
)

display_messages()

question = st.chat_input(
    "Ask anything from your documents..."
)

if question:

    add_user_message(question)

    with st.chat_message("user"):

        st.markdown(question)

    with st.chat_message("assistant"):

        generator = api.stream_chat(question)

        answer, citations = stream_generator(generator)

        if citations:

            st.divider()

            st.markdown("### 📚 Sources")

            for citation in citations:

                st.markdown(
                    f"- `{citation['source']}`"
                )

    add_assistant_message(answer)