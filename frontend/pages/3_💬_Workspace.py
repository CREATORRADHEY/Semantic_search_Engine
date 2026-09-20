import os
import sys
import streamlit as st

PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../..")
)

if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from frontend.utils.api_client import api

st.title("💬 Collection Workspace")

collections = [
    "AI",
    "Finance",
    "Legal",
    "General"
]

workspace = st.selectbox(
    "Active Workspace",
    collections
)

st.success(
    f"Current Workspace: {workspace}"
)

question = st.chat_input(
    "Ask only inside this workspace..."
)

if question:

    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):

        response = api.chat(question)

        st.markdown(response["answer"])

        if response["citations"]:

            st.markdown("### Sources")

            for citation in response["citations"]:

                st.write(citation["source"])