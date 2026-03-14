from binance.client import Client
from bot.logging_config import logger

def get_binance_client(api_key, api_secret):
    try:
        client = Client(api_key, api_secret, testnet=True)
        client.FUTURES_URL = 'https://testnet.binancefuture.com/fapi'
        logger.info("Binance client successfully initialized on Testnet.")
        return client
    except Exception as e:
        logger.error(f"Failed to initialize client: {e}")
        raise