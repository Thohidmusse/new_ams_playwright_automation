from dotenv import load_dotenv
import os

def load_config():  
    """
    Load configuration settings from environment variables.

    This function loads environment variables from a .env file and constructs
    a configuration dictionary based on the current environment (default is 'QA').
    The environment is determined by the 'AMS_ENVIRONMENT' variable, and the
    configuration keys are prefixed with the environment name.

    Returns:
        dict: A dictionary containing the following keys:
            - 'USERNAME': The AMS username for the current environment.
            - 'PASSWORD': The AMS password for the current environment.
            - 'BASE_URL': The base URL for the AMS application in the current environment.
    """
    load_dotenv() # Load environment variables from .env file 
    environment = os.getenv("AMS_ENVIRONMENT", "qa").upper() # Default to 'QA' if not set 
    prefix = f"{environment}_" 
    config = { 
              'USERNAME': os.getenv(f"{prefix}AMS_USERNAME"), 
              'PASSWORD': os.getenv(f"{prefix}AMS_PASSWORD"), 
              'BASE_URL': os.getenv(f"{prefix}BASE_URL") } 
    return config

# from dotenv import load_dotenv
# import os

# load_dotenv()  # Load environment variables from .env file

# USERNAME = os.getenv("AMS_USERNAME")
# PASSWORD = os.getenv("AMS_PASSWORD")

# BASE_URL = "https://amsui-qa.qwalton.com" 