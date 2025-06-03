import pandas as pd
import ta

def add_technical_indicators(df):
    df = df.copy()
    df['rsi'] = ta.momentum.RSIIndicator(df['Close']).rsi()
    df['macd'] = ta.trend.MACD(df['Close']).macd()
    df['sma_10'] = df['Close'].rolling(window=10).mean()
    df['sma_50'] = df['Close'].rolling(window=50).mean()
    df.dropna(inplace=True)
    return df
