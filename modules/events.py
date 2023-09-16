"""
main python file for events and handling communication to gpt and get abstract
"""

import streamlit as st

from .prompt import ask_gpt, new_question
from .utilities import get_abstract

def trigger_event(user_open_api_token):
    """
    Trigger the event for every user input.
    
    Returns:
        list: List of messages.
    """
    # check if the question need source
    session_message = new_question(user_open_api_token, st.session_state.messages)
    if session_message.lower() != "empty":
        abstract_list = get_abstract(input_str=session_message,
                                    weaviate_url='https://genta-academic-assistant-cluster-4vw2zql4.weaviate.network',
                                    openai_api_token=user_open_api_token)
    else:
        abstract_list = []
    # go to function from farrel
    # user_message: list(dict) -> [{"role": "system" or "assistant" or "user", "content": str}]
    new_user_message = ask_gpt(st.session_state.token, st.session_state.messages, abstract_list)

    return new_user_message
