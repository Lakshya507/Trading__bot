import argparse
import os
from dotenv import load_dotenv
from bot.client import get_binance_client
from bot.validators import validate_inputs
from bot.orders import place_order

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--symbol', required=True)
    parser.add_argument('--side', required=True, choices=['BUY', 'SELL'])
    parser.add_argument('--type', required=True, choices=['MARKET', 'LIMIT'], dest='order_type')
    parser.add_argument('--quantity', required=True, type=float)
    parser.add_argument('--price', type=float)
    
    args = parser.parse_args()
    load_dotenv()
    api_key = os.getenv('BINANCE_API_KEY')
    api_secret = os.getenv('BINANCE_API_SECRET')

    if not api_key or not api_secret:
        print("Error: API credentials missing.")
        return

    print(f"\n--- Order Request Summary ---")
    print(f"Symbol:   {args.symbol.upper()}")
    print(f"Side:     {args.side.upper()}")
    print(f"Type:     {args.order_type.upper()}")
    print(f"Quantity: {args.quantity}")
    if args.order_type.upper() == 'LIMIT':
        print(f"Price:    {args.price}")
    print("-----------------------------\n")

    try:
        validate_inputs(args.symbol, args.side, args.order_type, args.quantity, args.price)
        client = get_binance_client(api_key, api_secret)
        response = place_order(client, args.symbol, args.side, args.order_type, args.quantity, args.price)
        
        print("✅ SUCCESS: Order placed!")
        print(f"Order ID:     {response.get('orderId')}")
        print(f"Status:       {response.get('status')}")
        print(f"Executed Qty: {response.get('executedQty')}")
    except Exception as e:
        print(f"❌ FAILED: {e}")

if __name__ == '__main__':
    main()