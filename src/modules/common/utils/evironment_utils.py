import os
from dotenv import load_dotenv

def get_env_value(key: str) -> str:
    """
        Return value of environment variable key.

    params:
        key (str): Key of variable to get

    throws:
        Exception: If variable returns None (does not exist)

    returns:
        str: Value of the variable
    """
    env_value = os.environ.get(key)
    
    if env_value is None:
        raise Exception(f"Unable to find environment variable {env_value}")
    return env_value

def load_env(path: str) -> None:
    """
        Load a .env file at a configured path.
        
        params:
            path (str): Absolute or relative path to .env file
    """
    load_dotenv(path)
    