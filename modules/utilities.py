import requests

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
