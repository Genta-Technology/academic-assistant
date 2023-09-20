"""
A collection of utility functions.
"""

import os
import openai
import weaviate
import requests

from dotenv import load_dotenv, find_dotenv


def validate_openai_api_key(api_key: str) -> bool:
    """
    Validate OpenAI API Key

    Returns:
        bool: True if valid, False otherwise.
    """

    openai_api_endpoint = "https://api.openai.com/v1/engines"

    headers = {"Authorization": f"Bearer {api_key}"}

    response = requests.get(openai_api_endpoint, headers=headers, timeout=10)

    # Check the status code of the response
    return response.status_code == 200


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
        additional_headers={"X-OpenAI-Api-Key": openai_api_token}
    )

    response = (client.query
                .get("Paper", ["dOI", "authors", "abstract", "date", "title"])
                .with_near_vector({"vector": input_emb})
                .with_additional(['certainty'])
                .with_limit(top_n)
                .do())

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

    def __getitem__(self, key: str) -> str:
        """
        Get an environment variable.

        Args:
            key (str): Environment variable key.

        Returns:
            str: Environment variable value.
        """

        return self.get(key)

def search_semantics(querry, total=20):
    """
    search the querry using the semantics api

    Args:
    - querry (str)
    - total (int) (between 1-10, set default to 5) [optional]
    """
    url_search = "https://api.semanticscholar.org/graph/v1/paper" + \
                 f"/search?query={querry.replace(' ', '+').replace('-', ' ')}&limit=" + \
                 f"{total}&fields=abstract,authors,year,externalIds" + \
                 ",title,publicationDate"

    result = requests.get(url_search, timeout=10)

    docs = []
    if result.status_code == 200:
        result = result.json()
        for i in range(len(result["data"])):
            if "DOI" not in result["data"][i]['externalIds'] or \
                result["data"][i]["abstract"] is None:
                continue

            doc = {
                "dOI": result["data"][i]["externalIds"]["DOI"], 
                "abstract": result["data"][i]["abstract"],
                "title":result["data"][i]["title"],
                "date":result["data"][i]["publicationDate"],
                "authors":get_authors(result["data"][i]["authors"])
            }
            docs += [doc]

    return docs[:5]

def get_authors(list_author):
    """
    consumed list of dictionary author and return just list of authors name

    Args:
    - list_author (list)
    """
    new_list = []

    for i in list_author:
        new_list += [i["name"]]

    return new_list
