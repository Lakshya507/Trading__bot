import logging
import os

def setup_logger():
    os.makedirs('logs', exist_ok=True)
    
    logger = logging.getLogger('TradingBot')
    logger.setLevel(logging.DEBUG)
    # File Handler
    file_handler = logging.FileHandler('logs/trading_bot.log')

    file_handler.setLevel(logging.DEBUG)

    # Console Handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)

    console_handler.setFormatter(formatter)

    if not logger.handlers:
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger

logger = setup_logger()