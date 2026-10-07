
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
      if short_sma.iloc[-1] > long_sma.iloc[-1]:
            return "BUY"
      else:
            return "HOLD"
#DO THIS FOR EVERY SYMBOL IN WATCHLIST
def main():
    for symbol in watchlist:
        stock_history = get_market_data(symbol)
        closing_prices = stock_history["Close"]
        short_sma = calculate_sma(closing_prices, 5)
        long_sma = calculate_sma(closing_prices, 20)
        signal = check_signal(short_sma, long_sma)
        if signal == "BUY":
            print(f"{symbol} BUY ALERT")
        else:
            print(f"{symbol} HOLD")

if __name__ == "__main__":
     main()

