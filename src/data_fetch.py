import yfinance as yf
import os

def fetch_stock_data(ticker):
    os.makedirs("data", exist_ok=True)

    df = yf.download(ticker, start="2020-01-01")
    df.to_csv("data/stock_data.csv")

    return df