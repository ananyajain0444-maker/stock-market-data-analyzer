import pandas as pd
import os

def process_data(df):
    os.makedirs("outputs", exist_ok=True)

    df.dropna(inplace=True)

    # Daily returns
    df["Daily Return"] = df["Close"].pct_change()

    # Moving averages
    df["MA20"] = df["Close"].rolling(20).mean()
    df["MA50"] = df["Close"].rolling(50).mean()

    # Volatility
    df["Volatility"] = df["Daily Return"].rolling(20).std()

    df.to_csv("outputs/processed_data.csv")

    return df


def generate_summary(df):
    os.makedirs("reports", exist_ok=True)

    summary = {
        "Highest Price": df["Close"].max(),
        "Lowest Price": df["Close"].min(),
        "Average Return": df["Daily Return"].mean(),
        "Volatility": df["Volatility"].mean()
    }

    summary_df = pd.DataFrame(summary.items(), columns=["Metric", "Value"])
    summary_df.to_csv("reports/report.csv", index=False)