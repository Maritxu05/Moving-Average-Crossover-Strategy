
def add_moving_averages (data, short_window =5, long_window=20):
    """
    Add short-term and long-term moving averages to the data.

    Args:
        data(pd.DataFrame) : Price data with 'Close' column
        short_window(int) : Short MA period (e.g. 20 days)
        long_window(int) : Long MA period (e.g. 50 days)
    """

    data ['SMA_short'] = data['Close'].rolling(window=short_window).mean()
    data ['SMA_long'] = data['Close'].rolling(window=long_window).mean()

def generate_signals (data):
    """
    Generate buy/sell signals beased on SMA crossover strategy.
    Returns a new 'Signal' column:
        1 = buy
       -1 = sell
        0 = hold
    """
    data['Signal'] = (data['SMA_short'] > data['SMA_long']).astype(int)
    # Buy = 1, Sell = -1, Hold = 0
    data['Position'] = data['Signal'].diff()
