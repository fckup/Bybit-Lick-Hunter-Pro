import json
import os
from dotenv import load_dotenv

def load_config():
    load_dotenv()  # Load environment variables from .env file
    config_path = os.getenv('CONFIG_PATH', 'config.json')
    with open(config_path, 'r') as f:
        config = json.load(f)
    return config
