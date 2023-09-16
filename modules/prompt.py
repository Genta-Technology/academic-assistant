"""
main python file for communicating with GPT and getting the response, main function is the com_gpt

Args:
    - token (str): 
    - messages (dict):
    - docs (list):
"""

import openai

MODEL = "gpt-3.5-turbo"
CONTEXT_NEW = "As an AI language model, your task is to provide a " +
              "detailed and scholarly response based on a given abstract: "
GOALS = "Your response should be focused on the mentioned specific question related to " +
        "the content of the abstracts. Your goal is to provide a comprehensive and well-informed " +
        "answer using the information from the provided abstracts. Please ensure that your response " +
        "is accurate, detailed, short answer, and relevant to the question asked. " +
        "In addition, if the question doesn't related to one of the abstract itself, " +
        "don't mentioned the abstract itself"

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

    return new_messages

def new_question(messages, docs):
    """
    first time asking gpt

    Args:
    - messages (dict)
    - docs (dict)
    """
    new_messages = add_system(messages, docs)
    output=openai.ChatCompletion.create(
        model=MODEL,
        messages=new_messages,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        )
    new_messages += [{"role": "assistant", "content":output['choices'][0]['message']['content']}]
    return new_messages

def con_question(messages):
    """
    continue asking gpt

    Args:
    - messages (dict)
    """
    output=openai.ChatCompletion.create(
        model=MODEL,
        messages=messages,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        )
    return messages + [{"role": "assistant", "content":output['choices'][0]['message']['content']}]

def add_system(messages, docs):
    """
    add system into messages

    Args:
    - messages (list)
    - docs (list)
    """
    prompt = CONTEXT_NEW + docs_compile(docs) + GOALS
    return [{"role": "system", "content": prompt}] + messages

def docs_compile(docs):
    """
    combined all abstracts and other supporting file into one

    Args:
    - docs (list)
    """
    combined_docs = ""
    j = 1

    for i in docs["data"]["Get"]["Paper"]:
        abstract, author, doi, date = abstract_to_string(i)
        abstract_context = ("Abstract " + str(j) + ":" + abstract +
                            ", the author of abstract " + str(j) + "is" + author +
                            ", with dOI number: " + doi +
                            ", with date published: " + date + ". ")
        combined_docs += abstract_context
        j += 1
    return combined_docs

def abstract_to_string(abstract_dict):
    """
    combined the dict of abstract into one string

    Args:
    - abstract (dict):
    """
    return (abstract_dict["abstract"] +
            abstract_dict["authors"] +
            abstract_dict["dOI"] +
            abstract_dict["date"])
    
