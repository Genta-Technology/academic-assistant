"""
FILE is for UI
"""

import streamlit as st

st.title("GENTA")

with st.sidebar:
    st.text_input("**Please enter token**", placeholder="Token", key="token")

if "token" not in st.session_state:
    st.session_state.token = ""

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Wassup"):
    with st.chat_message("user"):
        st.markdown(prompt)

    st.session_state.messages.append({"role": "user", "content": prompt})

    response = f"Echo : {prompt}"

    with st.chat_message("assistant"):
        st.markdown(response)

    st.session_state.messages.append({"role": "assistant", "content": response})