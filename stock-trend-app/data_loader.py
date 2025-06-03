import yfinance as yf

def get_stock_data(ticker, period='60d', interval='1d'):
    df = yf.download(ticker, period=period, interval=interval)
    df.dropna(inplace=True)
    return df
