import streamlit as st


def upload_success(filename):

    st.success(f"✅ {filename} indexed successfully.")


def upload_failed(filename):

    st.error(f"❌ Failed indexing {filename}")


def indexing_progress():

    return st.progress(0)