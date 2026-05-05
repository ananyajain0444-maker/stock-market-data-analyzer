import matplotlib.pyplot as plt
import seaborn as sns
import os

def generate_charts(df):
    os.makedirs("images", exist_ok=True)

    # Price chart
    plt.figure()
    df["Close"].plot(title="Stock Price")
    plt.savefig("images/price_chart.png")

    # Moving averages
    plt.figure()
    df[["Close", "MA20", "MA50"]].plot(title="Moving Averages")
    plt.savefig("images/moving_average.png")

    # Returns distribution
    plt.figure()
    sns.histplot(df["Daily Return"].dropna(), bins=50)
    plt.title("Returns Distribution")
    plt.savefig("images/returns.png")