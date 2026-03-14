# Binance Futures Testnet Trading Bot

This repository contains my submission for the **Python Developer Application Task**. It is a structured Python application designed to place orders on the **Binance Futures Testnet (USDT-M)**.

---

## Features

This bot fulfills all the core requirements and evaluation criteria outlined in the assignment:

* **MARKET and LIMIT Orders** — Successfully places both order types on the testnet.
* **BUY and SELL Support** — Supports both sides of a trade.
* **Input Validation** — Validates all CLI inputs before sending them to the API.
* **Clean Architecture** — Separation between API client, order logic, validators, and UI.
* **Logging** — API requests, responses, and errors are logged locally.
* **Error Handling** — Gracefully handles API errors, invalid inputs, and network failures.
* **Bonus Feature** — Includes a lightweight **Streamlit web UI**.

---

# Project Structure

```
trading_bot/
│
├── bot/                  # API layer and logic
│   ├── __init__.py
│   ├── client.py         # Binance client wrapper
│   ├── orders.py         # Order placement logic
│   ├── validators.py     # Input validation
│   └── logging_config.py # Logging configuration
│
├── logs/
│   └── trading_bot.log   # Generated logs containing MARKET and LIMIT order logs
│
├── cli.py                # CLI entry point
├── ui.py                 # Streamlit UI entry point
├── requirements.txt      # Project dependencies
├── .env                  # API credentials (not uploaded to Git)
└── README.md             # Documentation
```

---

# Setup

## 1. Create a Binance Futures Testnet Account

Register and activate a Binance Futures Testnet account.

Testnet URL:

```
https://testnet.binancefuture.com
```

---

## 2. Generate API Keys

After creating the account, generate your **Testnet API Key and Secret**.

These will be used by the bot to authenticate with the Binance API.

---

## 3. Clone the Repository

```
git clone <your-repository-link>
cd trading_bot
```

---

## 4. Create a Virtual Environment (Recommended)

```
python -m venv venv
```

Activate the environment.

Linux / Mac:

```
source venv/bin/activate
```

Windows:

```
venv\Scripts\activate
```

---

## 5. Install Dependencies

```
pip install -r requirements.txt
```

---

## 6. Configure API Credentials

Create a `.env` file in the root directory of the project.

```
BINANCE_API_KEY=your_testnet_api_key
BINANCE_API_SECRET=your_testnet_secret_key
```

---

# Running the Bot

## Option 1 — Command Line Interface (CLI)

Place a **Market BUY Order**

```
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.01
```

Place a **Limit SELL Order**

```
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.01 --price 90000
```

---

## Option 2 — Web UI (Streamlit)

Run the web interface:

```
streamlit run ui.py
```

A browser window will open automatically at:

```
http://localhost:8501
```

From the UI you can:

* Select trading symbol
* Choose order type
* Enter quantity
* Enter price for limit orders
* Execute BUY or SELL orders

---

# Logging

All bot activity is logged in:

```
logs/trading_bot.log
```

Logs include:

* API requests
* API responses
* Order placement results
* Errors and exceptions

---

# Assumptions

* The Binance Futures Testnet account has sufficient **USDT balance**.
* Binance enforces a **minimum notional value of $100 per order**.
* Example orders use `0.01 BTC` to exceed this threshold.
* Price and quantity values are converted to strings to avoid floating-point precision issues.

---

# Author

Lakshya
