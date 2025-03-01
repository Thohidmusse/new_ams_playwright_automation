from dotenv import load_dotenv
import os

def load_config(role="ASSESSOR"):  
    """
    Load configuration settings from environment variables for a given role.

    This function loads environment variables from a .env file and constructs
    a configuration dictionary based on the current environment and role.
    The environment is determined by the 'AMS_ENVIRONMENT' variable (default is 'QA').

    Args:
        role (str): Role for which to load credentials (e.g., 'ADMIN', 'ORG_ADMIN', 'SCIENCE_STAFF').

    Returns:
        dict: A dictionary containing:
            - 'USERNAME': The username for the given role and environment.
            - 'PASSWORD': The password for the given role and environment.
            - 'BASE_URL': The base URL for the AMS application in the current environment.
    """
    load_dotenv()  # Load environment variables from .env file

    # Get environment (default to 'qa')
    environment = os.getenv("AMS_ENVIRONMENT", "qa").upper()

    # Common base URL for all roles in the environment
    base_url = os.getenv(f"{environment}_BASE_URL")

    # Map roles to environment variable keys
    role_mapping = {
        "ADMIN": f"{environment}_AMS_USERNAME",
        "ORG_ADMIN": f"{environment}_ORG_ADMIN_USERNAME",
        "SCIENCE_STAFF": f"{environment}_SCIENCE_STAFF_USERNAME",
        "ASSESSOR": f"{environment}_ASSESSOR_USERNAME",
    }

    # Fallback if unexpected role is passed
    if role not in role_mapping:
        raise ValueError(f"Unsupported role: {role}")

    username_key = role_mapping[role]
    password_key = username_key.replace("USERNAME", "PASSWORD")

    # Build config dictionary
    config = {
        'USERNAME': os.getenv(username_key),
        'PASSWORD': os.getenv(password_key),
        'BASE_URL': base_url
    }
    return config