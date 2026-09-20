import streamlit as st


def stream_generator(generator):

    placeholder = st.empty()

    full_response = ""

    citations = []

    for token in generator:

        if token.startswith("\n[CITATIONS]"):

            citations = eval(
                token.replace(
                    "\n[CITATIONS]",
                    ""
                )
            )

            continue

        full_response += token

        placeholder.markdown(full_response + "▌")

    placeholder.markdown(full_response)

    return full_response, citations