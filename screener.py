
import os
from pathlib import Path

import requests
import yfinance as yf
from dotenv import load_dotenv

# CONFIGURATION
env_path = Path(__file__).parent / '.env'
load_dotenv(dotenv_path=env_path)
webhook_url = os.environ.get("DISCORD_WEBHOOK_URL")

watchlist = ["NVDA", "AMZN", "MSFT", "AUDUSD=X"]

#PROCESS EACH ASSET/PAIR
for symbol in watchlist:
    #Get market data
    ticker = yf.Ticker(symbol)
    stock_history = ticker.history(period="1mo")

#CALCULATE INDICATORS
    closing_prices = stock_history["Close"]

    short_sma = closing_prices.rolling(window=5).mean()
    long_sma = closing_prices.rolling(window=20).mean()

    latest_short = short_sma.iloc[-1]
    latest_long = long_sma.iloc[-1]

#MAKE DECISION
    if latest_short > latest_long:
        print(f"{symbol} BUY ALERT")

        # SEND NOTIFICATION
        payload = {
            "content": (
                f"**Quant Alert**: "
                f"'{symbol}' has triggered a technical BUY signal!"
            )
        }
        webhook_url = os.environ.get("DISCORD_WEBHOOK_URL")
        if webhook_url:
            requests.post(webhook_url, json=payload)


    else:
        print(f"{symbol} HOLD")


