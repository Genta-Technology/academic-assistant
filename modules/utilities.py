"""
A collection of utility functions.
"""

import os
import openai
import weaviate

from dotenv import load_dotenv, find_dotenv


def open_ai_embeddings(input_str: str, api_token: str):
    """Get the OpenAI embeddings for a given input string.

    :param input_str: Input string.
    :type input_str: str
    :param api_token: OpenAI API token.
    :type api_token: str
    :param input_str: str:
    :param api_token: str:
    :returns: List of embeddings.
    :rtype: list

    """

    # use the api token
    openai.api_key = api_token

    # convert text to embedding
    model_id = "text-embedding-ada-002"
    embedding = openai.Embedding.create(input=input_str,
                                        model=model_id)["data"][0]["embedding"]
    return embedding


def get_abstract(input_str: str,
                 weaviate_url: str,
                 openai_api_token: str,
                 top_n: int = 5):
    """Get the abstract of the top n papers similar to the input string.

    :param input_str: Input string.
    :type input_str: str
    :param weaviate_url: Weaviate URL.
    :type weaviate_url: str
    :param openai_api_token: OpenAI API token.
    :type openai_api_token: str
    :param n: Number of papers to return.
    :type n: int
    :param input_str: str:
    :param weaviate_url: str:
    :param openai_api_token: str:
    :param top_n: int:  (Default value = 5)
    :returns: List of papers.
    :rtype: list

    """

    input_emb = open_ai_embeddings(input_str, openai_api_token)

    client = weaviate.Client(
        url=weaviate_url,
        additional_headers={"X-OpenAI-Api-Key": openai_api_token})
    response = (client.query.get(
        "Paper", ["dOI", "authors", "abstract", "date"]).with_near_vector({
            "vector":
            input_emb
        }).with_limit(top_n).do())
    return response["data"]["Get"]["Paper"]


class EnvironmentVariables:
    """
    This class is used to load environment variables from a .env file.
    """

    def __init__(self):
        """
        Initialize the class.
        """

        # Load environment variables from .env file
        self.env_file = find_dotenv()
        if self.env_file:
            load_dotenv(self.env_file)

    def get(self, key: str) -> str:
        """
        Get an environment variable.

        Args:
            key (str): Environment variable key.

        Returns:
            str: Environment variable value.
        """

        return os.environ.get(key)

    def __call__(self, key: str) -> str:
        """
        Get an environment variable.

        Args:
            key (str): Environment variable key.

        Returns:
            str: Environment variable value.
        """

        return self.get(key)


env = EnvironmentVariables()
