"""
FILE is for UI
"""

import streamlit as st

from PIL import Image
from modules.utilities import validate_openai_api_key





TITLE =( '<link rel="stylesheet" type="text/css"'+
'href="http://fonts.googleapis.com/css?family=Ubuntu:regular,bold&subset=Latin">' + 
'<H1 style="font-family:Ubuntu; font-size: 30px; font-weight:bold;">' +
'<span style="font-size = 40px;">GENTA</span> - Academic Assitant</H1>')
st.markdown(TITLE, unsafe_allow_html=True)
st.markdown("""Genta Acadmic Assistant is a tool to help you""" +
""" find the right research paper for your research.""")

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
    BOX = '<style>#input {box-shadow: 10px 5px 5px black;}</style>'
    st.markdown(BOX, unsafe_allow_html=True)
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
            with st.expander("sources:"):
                st.write("test1")
                st.write("test2")
                st.write("test3")

        st.session_state.messages.append({"role": "user", "content": prompt})

        response = f"Echo : {prompt}"

        with st.chat_message("assistant"):
            st.markdown(response)

        st.session_state.messages.append({"role": "assistant", "content": response})
        
else:
    TEXT = ('<p style="font-size: 18px; font-weight:bold; color: #FF1D2E; margin-top: 15px;">'+
    'Please enter your OpenAI API TOKEN first in the sidebar to use this application</p>')
    st.markdown(TEXT, unsafe_allow_html=True)
