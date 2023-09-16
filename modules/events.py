from .utilities import get_abstract

def trigger_event(user_message, user_open_api_token, session):
    if not session:
        abstract_list = get_abstract(input_str=user_message, 
                                     weaviate_url='https://genta-academic-assistant-cluster-4vw2zql4.weaviate.network',
                                     openai_api_token=user_open_api_token)
    else:
        abstract_list = []
    # go to function from farrel
    """
    user_message: list(dict) -> [{"role": "system" or "assistant" or "user", "content": str}]
    """
    new_user_message = ask_gpt(user_open_api_token, user_message, abstract_list)