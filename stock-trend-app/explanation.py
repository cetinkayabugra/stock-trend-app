def generate_explanation(row):
    if row['rsi'] < 30:
        return "RSI < 30: Market may be oversold. Consider buying."
    elif row['rsi'] > 70:
        return "RSI > 70: Market may be overbought. Consider selling."
    else:
        return "No strong RSI signal. Hold."
