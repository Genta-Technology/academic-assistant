"""
FILE is for UI
"""

import streamlit as st

from modules.utilities import validate_openai_api_key

st.title("GENTA - Academic Assitant")
st.write("Genta Acadmic Assistant is a tool to help you find the right research paper for your research.")

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
    st.text_input("Please enter token", placeholder="Token", key="token", on_change=on_token_change)

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if st.session_state.token:
    if prompt := st.chat_input("Wassup"):
        with st.chat_message("user"):
            st.markdown(prompt)

        st.session_state.messages.append({"role": "user", "content": prompt})

        response = f"Echo : {prompt}"

        with st.chat_message("assistant"):
            st.markdown(response)

        st.session_state.messages.append({"role": "assistant", "content": response})
else:
    st.write("Please enter your OpenAI API TOKEN first in the sidebar to use this application")