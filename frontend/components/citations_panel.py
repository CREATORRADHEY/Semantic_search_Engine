import streamlit as st


def render_citations(citations):

    if not citations:
        return

    st.markdown("### 📚 Sources Used")

    for citation in citations:

        with st.container(border=True):

            st.markdown(
                f"**📄 {citation['source']}**"
            )

            st.caption(
                citation.get(
                    "snippet",
                    "Relevant document chunk."
                )
            )