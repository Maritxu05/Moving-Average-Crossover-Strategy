import matplotlib.pyplot as plt

def plot_performance(data):
    plt.figure(figsize=(12,6))
    (1 + data['Market_Returns']).cumprod().plot(label='Market')
    (1 + data['Strategy_Returns']).cumprod().plot(label='Strategy')
    plt.title('Strategy vs Market performance')
    plt.xlabel('Date')
    plt.ylabel('Growth of 1€')
    plt.legend()
    plt.grid(True)
    plt.show()

def plot_signals(data):
    """
    Plots the stock close price along with buy and sell signals.
    Assumes the data has 'Close', 'SMA_short', 'SMA_long', and 'Signal' columns.
    """
    plt.figure(figsize=(14,7))
    
    # Plot closing price
    plt.plot(data.index, data['Close'], label='Close Price', color='blue', alpha=0.5)
    
    # Plot moving averages
    plt.plot(data.index, data['SMA_short'], label='Short-term SMA', color='orange', linestyle='--')
    plt.plot(data.index, data['SMA_long'], label='Long-term SMA', color='purple', linestyle='--')
    
    # Calculate signal changes (buy/sell)
    data['Position'] = data['Signal'].diff()
    
    # Plot buy signals (Signal changes from 0 → 1)
    plt.plot(data[data['Position'] == 1].index,
             data['Close'][data['Position'] == 1],
             '^', markersize=12, color='green', label='Buy Signal')
    
    # Plot sell signals (Signal changes from 1 → 0)
    plt.plot(data[data['Position'] == -1].index,
             data['Close'][data['Position'] == -1],
             'v', markersize=12, color='red', label='Sell Signal')

    plt.title('Stock Price with Buy/Sell Signals')
    plt.xlabel('Date')
    plt.ylabel('Price (€)')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()