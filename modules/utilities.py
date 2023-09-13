import os

from dotenv import load_dotenv, find_dotenv

class EnvironmentVariables:
    """
    This class is used to load environment variables from a .env file.
    """

    def __init__(self):
        """
        Initialize the class.
        """

        # Load environment variables from .env file
        self.ENV_FILE = find_dotenv()
        if self.ENV_FILE:
            load_dotenv(self.ENV_FILE)

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