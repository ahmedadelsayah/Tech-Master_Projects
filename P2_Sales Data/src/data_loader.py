import pandas as pd


def load_and_clean_data(path="sales_data.csv"):
    """Loads CSV sales data, converts order dates, and extracts year/month."""
    df = pd.read_csv(path, encoding="latin1")
    df.dropna(subset=["Sales", "Order Date"], inplace=True)
    df["Order Date"] = pd.to_datetime(df["Order Date"], errors="coerce")
    df["Year"] = df["Order Date"].dt.year
    df["Month"] = df["Order Date"].dt.month
    return df