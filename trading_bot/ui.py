import streamlit as st
import os
import datetime
from dotenv import load_dotenv
from bot.client import get_binance_client
from bot.validators import validate_inputs
from bot.orders import place_order

load_dotenv()
api_key = os.getenv('BINANCE_API_KEY')
api_secret = os.getenv('BINANCE_API_SECRET')

st.set_page_config(page_title="Binance Testnet Bot", layout="centered")
st.title("📈 Binance Testnet Bot")

with st.form("trading_form"):
    symbol = st.text_input("Symbol", value="BTCUSDT").upper()
    col1, col2 = st.columns(2)
    with col1:
        side = st.selectbox("Side", ["BUY", "SELL"])
    with col2:
        order_type = st.selectbox("Order Type", ["MARKET", "LIMIT"])
    
    quantity = st.number_input("Quantity", min_value=0.001, value=0.01, step=0.001, format="%.3f")
    price = st.number_input("Price (for LIMIT)", min_value=0.0, value=50000.0, step=100.0)
    submit_button = st.form_submit_button("Place Order")

if submit_button:
    if not api_key or not api_secret:
        st.error("❌ API credentials not found.")
    else:
        try:
            final_price = price if order_type == "LIMIT" else None
            validate_inputs(symbol, side, order_type, quantity, final_price)
            client = get_binance_client(api_key, api_secret)
            
            with st.spinner("Sending order..."):
                response = place_order(client, symbol, side, order_type, quantity, final_price)
                
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            st.success(f"✅ {order_type} Order placed at {current_time}!")
            st.json({
                "Order ID": response.get("orderId"),
                "Status": response.get("status"),
                "Executed Qty": response.get("executedQty")
            })
        except Exception as e:
            st.error(f"❌ Failed: {e}")