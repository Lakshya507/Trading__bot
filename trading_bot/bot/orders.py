from bot.logging_config import logger
from binance.exceptions import BinanceAPIException

def place_order(client, symbol, side, order_type, quantity, price=None):
    try:
        logger.info(f"Preparing {order_type} order for {quantity} {symbol} ({side})")
        order_params = {
            'symbol': symbol.upper(),
            'side': side.upper(),
            'type': order_type.upper(),
            'quantity': quantity
        }
        if order_type.upper() == 'LIMIT':
            order_params['price'] = price
            order_params['timeInForce'] = 'GTC'

        response = client.futures_create_order(**order_params)
        logger.info(f"API Response: {response}")
        return response
    except BinanceAPIException as e:
        logger.error(f"Binance API Error: {e.status_code} - {e.message}")
        raise
    except Exception as e:
        logger.error(f"System Error: {e}")
        raise