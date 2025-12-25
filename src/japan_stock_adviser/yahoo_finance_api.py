import sys

import yfinance


def get_data():
    symbol = sys.argv[1]
    ticker_data = yfinance.Ticker(f"{symbol}.T")
    basic_info = ticker_data.info
    print(basic_info)
