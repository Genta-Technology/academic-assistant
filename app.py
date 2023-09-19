"""
FILE is for UI
"""
import streamlit as st
from PIL import Image

from modules.events import trigger_event
from modules.utilities import EnvironmentVariables, validate_openai_api_key

env = EnvironmentVariables()

IMAGE_DIRECTORY = "./Genta_Logo.png"
image = Image.open(IMAGE_DIRECTORY)

PAGE_CONFIG = {"page_title": "Academic Assistant", "page_icon": image}

st.set_page_config(**PAGE_CONFIG)

TITLE = (
    '<link rel="stylesheet" type="text/css"'
    + 'href="http://fonts.googleapis.com/css?family=Ubuntu:regular,bold&subset=Latin">'
    + '<H1 style="font-family:Ubuntu; font-size: 30px; font-weight:bold;">'
    + '<span style="font-size = 40px;">GENTA</span> - Academic Assistant</H1>'
)

st.markdown(TITLE, unsafe_allow_html=True)
st.markdown(
    """Genta Acadmic Assistant is a tool to help you"""
    + """ find the right research paper for your research."""
)

with st.sidebar:
    col1, col2, col3 = st.columns(3)
    img = Image.open("Extension.png")
    with col2:
        st.image(img, use_column_width="always")
    BOX = "<style>#input {box-shadow: 10px 5px 5px black;}</style>"
    st.markdown(BOX, unsafe_allow_html=True)
    st.text_input(
        "Please enter token",
        placeholder="Optional",
        key="token",
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

if (
    len(st.session_state.messages) <= 8
    and ("token" in st.session_state or st.session_state.token == "")
) or (validate_openai_api_key(st.session_state.token) and "token" in st.session_state):
    if prompt := st.chat_input("Wassup"):
        with st.chat_message("user"):
            st.markdown(prompt)

        st.session_state.messages.append({"role": "user", "content": prompt})

        response, docs = trigger_event(
            st.session_state.token
            if "token" in st.session_state
            and validate_openai_api_key(st.session_state.token)
            else env["OPENAI_API_KEY"]
        )

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
        + "Limit exceeded, refresh the page to start a new conversation or insert your own"
        + " <a href='https://platform.openai.com/account/api-keys'>OpenAI API key</a> "
        + "in the sidebar.</p>"
    )
    st.markdown(TEXT, unsafe_allow_html=True)
