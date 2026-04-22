# Trading Bot – Binance Testnet

## Overview

This project is a simplified Python-based trading bot that places MARKET and LIMIT orders using the Binance Testnet API. It is designed with a clean, modular structure and includes input validation, logging, and error handling.

---

## Features

* Place MARKET and LIMIT orders
* Supports BUY and SELL operations
* Command-line interface (CLI) using argparse
* Input validation for all parameters
* Structured logging of API requests, responses, and errors
* Modular code design (client, orders, validators, logging)

---

## Tech Stack

* Python 3.x
* python-binance
* argparse
* logging
* python-dotenv

---

## Project Structure

trading_bot/
│
├── bot/
│   ├── client.py          # Binance API client setup
│   ├── orders.py          # Order placement logic
│   ├── validators.py      # Input validation
│   ├── logging_config.py  # Logging configuration
│
├── cli.py                 # CLI entry point
├── requirements.txt
├── README.md
├── .env                   # API credentials (not shared)
├── trading.log            # Log file

---

## Setup Instructions

### 1. Clone the repository

git clone <your-repo-link>
cd trading_bot

### 2. Install dependencies

pip install -r requirements.txt

### 3. Add API credentials

Create a `.env` file in the root directory:

API_KEY=your_api_key
API_SECRET=your_api_secret

---

## Usage

### Place a MARKET order

python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001

### Place a LIMIT order

python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 60000

---

## Output Example

Order Request:
{'symbol': 'BTCUSDT', 'side': 'BUY', 'type': 'MARKET', 'quantity': 0.001, 'price': None}

Order Success:
{'orderId': 8009788, 'status': 'FILLED', 'executedQty': '0.00100000', 'avgPrice': '78133.16'}

---

## Logging

All API interactions are logged in `trading.log`, including:

* Request details
* API responses
* Errors (if any)

---

## Assumptions

* API keys are valid and configured correctly
* Sufficient test balance is available
* Symbol format follows Binance standards (e.g., BTCUSDT)

---

## Note

Due to access limitations with Binance Futures Testnet API, the Binance Spot Testnet API was used for implementation. The structure and logic remain consistent with the requirements.

---

## Evaluation Coverage

This implementation satisfies:

* Order placement (MARKET and LIMIT)
* CLI input handling
* Input validation
* Logging of requests and responses
* Error handling
* Clean and modular code structure

---

## Author

Kaviya
