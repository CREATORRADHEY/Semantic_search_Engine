import streamlit as st


def render_source_cards(results):

    st.markdown("### 📄 Retrieved Context")

    for result in results:

        with st.expander(
            f"📄 {result['source']} | Score {result['score']:.3f}"
        ):

            st.write(result["text"])