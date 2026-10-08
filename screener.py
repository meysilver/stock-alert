
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
def get_market_data(symbol):
        #Get market data
        ticker = yf.Ticker(symbol)
        stock_history = ticker.history(period="1mo")
        return stock_history

#CALCULATE INDICATORS
def calculate_sma(prices, window):
    sma = prices.rolling(window=window).mean()
    return sma

def check_signal(short_sma, long_sma):
      valid_short_sma = short_sma.dropna()
      valid_long_sma = long_sma.dropna()
      if len(valid_short_sma) < 2 or len(valid_long_sma) < 2:
           return "HOLD"

      today_short = valid_short_sma.iloc[-1]
      yesterday_short = valid_short_sma.iloc[-2]
      today_long = valid_long_sma.iloc[-1]
      yesterday_long = valid_long_sma.iloc[-2]


      if yesterday_short <= yesterday_long and today_short > today_long:
            return "BUY"
      elif yesterday_short >= yesterday_long and today_short < today_long:
           return "SELL"
      else:
            return "HOLD"

def send_alert(symbol, signal):
     message = (
        f"**Quant Alert**: "
        f"'{symbol}' has triggered a technical {signal} signal!"
     )
     payload = {
        "content": message
     }
     try:
        response = requests.post(webhook_url, json=payload, timeout=10)
        response.raise_for_status()
     except requests.RequestException as error:
        print(f"Failed to send Discord alert: {error}")
#DO THIS FOR EVERY SYMBOL IN WATCHLIST
def main():
    for symbol in watchlist:
        stock_history = get_market_data(symbol)
        closing_prices = stock_history["Close"]
        short_sma = calculate_sma(closing_prices, 5)
        long_sma = calculate_sma(closing_prices, 20)
        signal = check_signal(short_sma, long_sma)
        print(f"{symbol} {signal}")
        send_alert(symbol, signal)


if __name__ == "__main__":
     main()

