import streamlit as st


def document_card(document):

    with st.container(border=True):

        st.markdown(
            f"### 📄 {document.filename}"
        )

        st.caption(document.category)

        st.write(document.source)

        st.metric(
            "Chunks",
            document.chunks
        )