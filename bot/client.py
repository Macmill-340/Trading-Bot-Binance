import os
from binance import Client
from dotenv import load_dotenv
from bot.logging_config import setup_logging

load_dotenv()

logger = setup_logging()

def get_client():
    api_key = os.getenv("API_KEY")
    api_secret = os.getenv("SECRET_KEY")

    if not api_key or not api_secret:
        logger.error("API credentials missing. Please set API_KEY and API_SECRET.")
        raise ValueError("Missing API credentials.")

    client = Client(api_key, api_secret, testnet=True)
    return client