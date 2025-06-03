import streamlit as st
import matplotlib.pyplot as plt
from data_loader import get_stock_data
from features import add_technical_indicators
from model import train_model
from explanation import generate_explanation

st.title("📈 Stock Trend Analyzer")

ticker = st.text_input("Enter Stock Ticker", "AAPL")

if ticker:
    df = get_stock_data(ticker)
    df = add_technical_indicators(df)
    model = train_model(df)

    last_row = df.iloc[-1:]
    prediction = model.predict(last_row[['rsi', 'macd', 'sma_10', 'sma_50']])[0]
    signal = "📥 BUY" if prediction == 1 else "📤 SELL"

    explanation = generate_explanation(last_row.iloc[0])

    st.subheader(f"Prediction: {signal}")
    st.write(explanation)

    st.line_chart(df['Close'])
