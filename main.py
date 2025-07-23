import yfinance as yf
import pandas as pd
from data_loader import download_and_save
from data_loader import load_data
from strategy import add_moving_averages
from strategy import generate_signals
from backtest import backtest
from metrics import plot_performance
from metrics import plot_signals

def main():
    ticker = 'AAPL'
    start_date = '2019-01-01'
    end_date = '2024-01-01'
    csv_file = 'AAPL.csv'

    #Step 1: Dowload and save stock data (run this once)
    download_and_save(ticker, start_date,end_date, csv_file)

    #Step 2: Load data from CSV
    data = load_data(csv_file)

    add_moving_averages(data)

    generate_signals(data)

    backtest(data)

    plot_performance(data)

    plot_signals(data)
    #Now you can add more code here to analyze or run strategies on data
    #For exmaple moving averages or backtest strategies.

if __name__ == '__main__':
    main()
    