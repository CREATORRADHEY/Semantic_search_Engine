import streamlit as st


def render_token_usage(question, answer):

    input_tokens = len(question.split())

    output_tokens = len(answer.split())

    total = input_tokens + output_tokens

    col1, col2, col3 = st.columns(3)

    col1.metric("Input Tokens", input_tokens)

    col2.metric("Output Tokens", output_tokens)

    col3.metric("Total Tokens", total) 
