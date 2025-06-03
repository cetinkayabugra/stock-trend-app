from sklearn.ensemble import RandomForestClassifier

def train_model(df):
    df['target'] = (df['Close'].shift(-1) > df['Close']).astype(int)
    X = df[['rsi', 'macd', 'sma_10', 'sma_50']]
    y = df['target']
    model = RandomForestClassifier()
    model.fit(X, y)
    return model
