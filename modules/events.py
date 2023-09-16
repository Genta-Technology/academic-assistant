import streamlit as st

from .utilities import get_abstract

def trigger_event(user_open_api_token):
    # check if there is system in session state
    if any(['system' in state.keys() for state in st.session_state.messages]):
        abstract_list = get_abstract(input_str=st.session_state.messages[-1]['content'], 
                                     weaviate_url='https://genta-academic-assistant-cluster-4vw2zql4.weaviate.network',
                                     openai_api_token=user_open_api_token)
    else:
        abstract_list = []
    # go to function from farrel
    """
    user_message: list(dict) -> [{"role": "system" or "assistant" or "user", "content": str}]
    """
    new_user_message = ask_gpt(user_open_api_token, st.session_state.messages, abstract_list)
