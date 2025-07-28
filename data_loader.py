import yfinance as yf
import pandas as pd
def download_and_save (ticker, start_date, end_date, filename):
    """
    Download historical stock data from Yahoo Finance and save as a CSV.

    Args:
        ticker (str) : Stock ticker symbol, e.g., 'AAPL'
        start_date (str) : Start date in 'YYYY-MM-DD'
        end_date (str) : End date in 'YYYY-MM-DD'
        filename (str) : Path to save CSV file
    """
    print(f"Downloading data for {ticker} from {start_date} to {end_date}")
    data = yf.download(
        ticker,
        start=start_date,
        end=end_date,
        progress=False,
        auto_adjust=True,   # Removes splits/dividends adjustments
        actions=False,      # Don't include dividends/splits
        group_by='ticker'   # This still avoids multi-level column structure
    )
    # Checks if the DataFrame has a MultiIndex 
    if isinstance(data.columns, pd.MultiIndex):
        # If true, flattens the column structure by taking only the second level of the MultiIndex
        data.columns = data.columns.get_level_values(1)
    data.to_csv(filename)
    print(f"Data saved to {filename}\n")

def load_data (file_path):
    """
    Load stock data CSV into a pandas DataFrame.
    Args:
        file_path(str): Path to CSV file
    Returns:
        pd.DataFrame : DataFrame containing stock data
    """
    print(f"Loading data from {file_path}")
    df = pd.read_csv(file_path, index_col=0, parse_dates=True)
    print (f"Data loaded! Here's a preview:\n{df.head()}\n")
    return df