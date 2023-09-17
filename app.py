"""
FILE is for UI
"""

import streamlit as st

from modules.events import trigger_event

st.title("GENTA")

with st.sidebar:
    st.text_input("**Please enter token**", placeholder="Token", key="token")

if "token" not in st.session_state:
    st.session_state.token = ""

if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "system", 
            "content":  'You will be provided with a document delimited by triple quotes and a question. ' + \
                        'Your task is to answer the question using only the provided document and to cite ' + \
                        'the passage(s) of the document used to answer the question. If the document does ' + \
                        'not contain the information needed to answer this question then simply write: ' + \
                        '"Insufficient information." If an answer to the question is provided, it must ' + \
                        'be annotated with a citation. Use the following format for to cite relevant passages ' + \
                        '({"citation": …}).'
        }
    ]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if st.session_state.token != "":
    if prompt := st.chat_input("Wassup"):
        with st.chat_message("user"):
            st.markdown(prompt)

        st.session_state.messages.append({"role": "user", "content": prompt})

        response = trigger_event()

        with st.chat_message("assistant"):
            st.markdown(response)

        st.session_state.messages.append({"role": "assistant", "content": response})