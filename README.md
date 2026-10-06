Quant Alert
A beginner Python project that monitors a watchlist of financial assets and generates technical alerts using moving averages.

What it does
The program:
- Takes a watchlist of financial assets.
- Retrieves one month of historical market data using yfinance.
- Extracts daily closing prices.
- Calculates a 5-day Simple Moving Average (SMA).
- Calculates a 20-day Simple Moving Average (SMA).
- Compares the two moving averages.
- Prints a BUY or HOLD signal.
- Sends a Discord notification when the BUY condition is met.

Example logic
## Architecture

```text
Watchlist
    │
    ▼
Get historical market data
    │
    ▼
Extract closing prices
    │
    ▼
Calculate 5-day SMA + 20-day SMA
    │
    ▼
Compare the two averages
    │
    ├───────────────┐
    │               │
    ▼               ▼
5-day > 20-day   5-day ≤ 20-day
    │               │
    ▼               ▼
BUY ALERT          HOLD
    │
    ▼
Discord notification
```

Technologies
Python
yfinance
pandas
requests
python-dotenv
Discord Webhooks

Project structure
stock-alert/
├── .gitignore
├── README.md
└── screener.py

The Discord webhook URL is stored locally in a .env file and is intentionally excluded from the public repository.

Disclaimer
This is an educational programming project, not financial advice or a production trading system.
