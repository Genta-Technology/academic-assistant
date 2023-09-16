"""
This module contains utility functions for the project.
"""

import weaviate
import openai

def open_ai_embeddings(input_str:str, api_token:str):
    """
    Get the OpenAI embeddings for a given input string.

    Args:
        input_str (str): Input string.
        api_token (str): OpenAI API token.

    Returns:
        list: List of embeddings.
    """

    # use the api token
    openai.api_key = api_token

    # convert text to embedding
    model_id = "text-embedding-ada-002"
    embedding = openai.Embedding.create(input=input_str, model=model_id)['data'][0]['embedding']
    return embedding

def get_abstract(input_str:str, weaviate_url: str, openai_api_token:str, top_n:int = 5):
    """
    Get the abstract of the top n papers similar to the input string.

    Args:
        input_str (str): Input string.
        weaviate_url (str): Weaviate URL.
        openai_api_token (str): OpenAI API token.
        n (int): Number of papers to return.

    Returns:
        list: List of papers.
    """
    
    input_emb = open_ai_embeddings(input_str, openai_api_token)

    client = weaviate.Client(
        url = weaviate_url,
        additional_headers={
            "X-OpenAI-Api-Key": openai_api_token
        }
    )
    response = (
        client.query
        .get("Paper", ["dOI", "authors", "abstract", "date"])
        .with_near_vector({'vector': input_emb})
        .with_limit(top_n)
        .do()
    )
    return response["data"]["Get"]["Paper"]
