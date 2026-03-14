def validate_inputs(symbol, side, order_type, quantity, price):
    if side.upper() not in ['BUY', 'SELL']:
        raise ValueError("Side must be 'BUY' or 'SELL'.")
    
    if order_type.upper() not in ['MARKET', 'LIMIT']:
        raise ValueError("Order type must be 'MARKET' or 'LIMIT'.")
    
    if float(quantity) <= 0:
        raise ValueError("Quantity must be greater than 0.")
    
    if order_type.upper() == 'LIMIT' and (price is None or float(price) <= 0):
        raise ValueError("A valid price is required for LIMIT orders.")
    
    return True