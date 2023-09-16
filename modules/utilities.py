import requests

def validate_openai_api_key(api_key: str) -> bool:
    """
    Validate OpenAI API Key

    Returns:
        bool: True if valid, False otherwise.
    """

    OPENAI_API_ENDPOINT = "https://api.openai.com/v1/engines"

    headers = {"Authorization": f"Bearer {api_key}"}

    response = requests.get(OPENAI_API_ENDPOINT, headers=headers)

    # Check the status code of the response
    return response.status_code == 200