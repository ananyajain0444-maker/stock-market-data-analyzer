from src.data_fetch import fetch_stock_data
from src.analysis import process_data, generate_summary
from src.visualization import generate_charts

def main():
    ticker = "AAPL"

    print("📥 Fetching stock data...")
    df = fetch_stock_data(ticker)

    print("🧹 Processing data...")
    df = process_data(df)

    print("📊 Generating charts...")
    generate_charts(df)

    print("📄 Generating report...")
    generate_summary(df)

    print("✅ Project completed successfully!")

if __name__ == "__main__":
    main()