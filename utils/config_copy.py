from dotenv import load_dotenv
import os

def load_config():  
    load_dotenv() # Load environment variables from .env file 
    environment = os.getenv("AMS_ENVIRONMENT", "qa").upper() # Default to 'QA' if not set 
    prefix = f"{environment}_" 
    config = { 
              'USERNAME': os.getenv(f"{prefix}AMS_USERNAME"), 
              'PASSWORD': os.getenv(f"{prefix}AMS_PASSWORD"), 
              'BASE_URL': os.getenv(f"{prefix}BASE_URL") } 
    return config