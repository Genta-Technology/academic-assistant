"""
FILE is for UI
"""

import streamlit as st
from PIL import Image

from modules.events import trigger_event
from modules.utilities import validate_openai_api_key

TITLE = (
    '<link rel="stylesheet" type="text/css"'
    + 'href="http://fonts.googleapis.com/css?family=Ubuntu:regular,bold&subset=Latin">'
    + '<H1 style="font-family:Ubuntu; font-size: 30px; font-weight:bold;">'
    + '<span style="font-size = 40px;">GENTA</span> - Academic Assitant</H1>'
)

st.markdown(TITLE, unsafe_allow_html=True)
st.markdown(
    """Genta Acadmic Assistant is a tool to help you"""
    + """ find the right research paper for your research."""
)


def on_token_change():
    """
    Callback for token change.

    Returns:
        None.
    """

    if not validate_openai_api_key(st.session_state.token):
        st.error("Invalid OpenAI API Key")
        del st.session_state.token


with st.sidebar:
    col1, col2, col3 = st.columns(3)
    img = Image.open("Extension.png")
    with col2:
        st.image(img, use_column_width="always")
    BOX = "<style>#input {box-shadow: 10px 5px 5px black;}</style>"
    st.markdown(BOX, unsafe_allow_html=True)
    st.text_input(
        "Please enter token",
        placeholder="Token",
        key="token",
        on_change=on_token_change,
    )

if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "system",
            "content": "You will be provided with multiple documents "
            + "delimited by triple quotes and a question. "
            + "Your task is to answer the question using only "
            + "the provided documents and to cite "
            + "the passage(s) of the documents used to answer "
            + "the question. If the documents does "
            + "not contain the information needed to "
            + "answer this question then simply write: "
            + '"Insufficient information." If an answer '
            + "to the question is provided, it must "
            + "be annotated with a citations. Use the following "
            + "format for to cite relevant passages "
            + '({"citations": ..., ..., ...}).',
        }
    ]

for message in st.session_state.messages[1:]:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if st.session_state.token:
    if prompt := st.chat_input("Wassup"):
        with st.chat_message("user"):
            st.markdown(prompt)

        st.session_state.messages.append({"role": "user", "content": prompt})

        response, docs = trigger_event()

        with st.chat_message("assistant"):
            st.markdown(response)
            with st.expander("Arxiv Search Results"):
                for doc in docs:
                    st.markdown(
                        f"<a href='https://arxiv.org/abs/{doc['dOI']}'>"
                        + f"{doc['title']}, {doc['authors']}, {doc['date']}</a>",
                        unsafe_allow_html=True,
                    )

        st.session_state.messages.append({"role": "assistant", "content": response})

else:
    TEXT = (
        '<p style="font-size: 18px; font-weight:bold; color: #FF1D2E; margin-top: 15px;">'
        + "Please enter your OpenAI API TOKEN first in the sidebar to use this application</p>"
    )
    st.markdown(TEXT, unsafe_allow_html=True)
