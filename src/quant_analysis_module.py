import pandas as pd
import numpy as np
import talib
import matplotlib.pyplot as plt
import seaborn as sns
import yfinance as yf
from pypfopt import expected_returns, risk_models, EfficientFrontier

def load_stock_data(filepath):
    df = pd.read_csv(filepath, parse_dates=['Date'])
    df = df.sort_values('Date')
    df.set_index('Date', inplace=True)
    return df

def apply_ta_indicators(df):
    df['SMA_20'] = talib.SMA(df['Close'], timeperiod=20)
    df['SMA_50'] = talib.SMA(df['Close'], timeperiod=50)
    df['RSI'] = talib.RSI(df['Close'], timeperiod=14)
    macd, macdsignal, macdhist = talib.MACD(df['Close'], fastperiod=12, slowperiod=26, signalperiod=9)
    df['MACD'] = macd
    df['MACD_Signal'] = macdsignal
    df['MACD_Hist'] = macdhist
    return df

def visualize_indicators(df):
    plt.figure(figsize=(14, 7))
    plt.plot(df['Close'], label='Close Price', alpha=0.5)
    plt.plot(df['SMA_20'], label='SMA 20')
    plt.plot(df['SMA_50'], label='SMA 50')
    plt.title("Stock Price with SMA")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(14, 4))
    plt.plot(df['RSI'], label='RSI')
    plt.axhline(70, color='red', linestyle='--')
    plt.axhline(30, color='green', linestyle='--')
    plt.title("RSI Indicator")
    plt.ylabel("RSI")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(14, 5))
    plt.plot(df['MACD'], label='MACD')
    plt.plot(df['MACD_Signal'], label='Signal Line')
    plt.bar(df.index, df['MACD_Hist'], label='Histogram', alpha=0.5)
    plt.title("MACD Indicator")
    plt.xlabel("Date")
    plt.ylabel("MACD")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def export_analysis(df, filename="stock_analysis_results.csv"):
    df.to_csv(filename)
    print(f"Exported stock analysis results to {filename}")
