"""
main python file for communicating with GPT and getting the response, main function is the com_gpt

Args:
    - token (str): 
    - messages (dict):
    - docs (list):
"""

import openai

MODEL = "gpt-3.5-turbo"
# PRE_SEARCH = "Based on the recent question, your task is to give me an " + \
#              "appropriate query to search arxiv paper, or only response with " + \
#              "EMPTY If the question does not need a sources to answer. You should " + \
#              "not say more than query. You should not say any words except the query or EMPTY."

PRE_SEARCH_SYSTEM = "You are an expert in finding research papers on the internet. " + \
                    "You are the master in creating perfect search queries. " + \
                    "You will be given the previous chat between you and the user. " + \
                    "Your task is to analyze the latest question and only provide an " + \
                    "appropriate query to search research papers such as Google " + \
                    "Scholar, Arxiv, and Semantic Scholars. Your response should be " + \
                    "only the search query, and you should not say more than the query " + \
                    "itself. If, based on your analysis of the previous chat, the latest " + \
                    "question does not need a search query or is only a small talk chat, " + \
                    "your response should be EMPTY. Once again, you should not say " + \
                    "any words except the query or EMPTY!"


def ask_gpt(token, messages, docs):
    """
    takes in user gpt token, session stage, and required documents (abstract) and return answer
    
    Args:
    - token (str): 
    - message (list):
    - docs (list):
    """
    # Auth Token
    openai.api_key = token

    #Intitial Question
    if len(docs) > 0:
        new_messages = new_question(messages, docs)

    #Continue asking
    else:
        new_messages = con_question(messages)

    return new_messages # String

def generate_search(token, messages):
    """
    generate search querries for abstract or return EMPTY if no question asked

    Args:
    - token (str)
    - messages (list)
    """
    # Auth Token
    openai.api_key = token

    search_system = [{"role":"system", "content":PRE_SEARCH_SYSTEM}]
    output=openai.ChatCompletion.create(
        model=MODEL,
        messages=search_system + messages[1:],
        temperature=1.3,
        max_tokens=256,
        )
    output = output['choices'][0]['message']['content']
    output = output if 'as an ai language' not in output.lower() else 'EMPTY'
    return output

def new_question(messages, docs):
    """
    first time asking gpt with docs/sources included

    Args:
    - messages (dict)
    - docs (dict)
    """
    messages = mod_new_messages(messages, docs)
    output=openai.ChatCompletion.create(
        model=MODEL,
        messages=messages,
        temperature=0.2,
        max_tokens=512,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        )
    # output = add_source(output, docs)
    messages += [{"role": "assistant", "content":output['choices'][0]['message']['content']}]
    return messages


def create_user_context(question, sources):
    """
    create user context for GPT

    Args:
    - question (str):
    - sources (list):
    """
    user_context = "My question is: " + question + ". " + \
                   "My sources are: " + sources + ". " + \
                   "Answer the question only if you can " + \
                   "find the answer in the sources. " + \
                   "If you can't find the answer in any of " + \
                   "the sources, response with " +\
                   "'i don't know the answer to this question " + \
                   "based on my current knowledge'. " + \
                   "Add the source of your answer as (authors, dOI) " + \
                   "for every text you get from the sources."

    return user_context

def con_question(messages):
    """
    continue asking gpt

    Args:
    - messages (dict)
    """
    output = openai.ChatCompletion.create(
        model=MODEL,
        messages=messages,
        temperature=0.2,
        max_tokens=512,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return messages + [{"role": "assistant", "content":output['choices'][0]['message']['content']}]

def mod_new_messages(messages, docs):
    """
    modify the new messages for adding context

    Args:
    - messages (list)
    - docs (list)
    """
    prompt = docs_compile(docs) + "\n Question: " + messages[-1]["content"]
    messages = messages[:-1]

    return messages + [{"role":"user", "content":prompt}]

def docs_compile(docs):
    """
    combined all abstracts and other supporting file into one

    Args:
    - docs (list)
    """
    combined_docs = '"""'

    for doc in docs:
        abstract, author, doi, date = abstract_to_string(doc)
        abstract_context = abstract +\
                            "\n {citation: " + f"{author}, {date}, {doi}" + "}\n"
        combined_docs += abstract_context
    return combined_docs + '"""'

def abstract_to_string(abstract_dict):
    """
    combined the dict of abstract into one string

    Args:
    - abstract (dict):
    """
    return (abstract_dict["abstract"],
            abstract_dict["authors"],
            abstract_dict["dOI"],
            abstract_dict["date"])
