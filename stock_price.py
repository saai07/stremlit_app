import pandas as pd
import streamlit as st
import yfinance as yf
import datetime

st.write(
    """
    # Stock Price Analyser
    Apple stock are shown
    """
)
col1 , col2 = st.columns(2)
ticker_symbol = st.text_input(
    "Enter a Stock symbol",
    "AAPL",
    key = "placeholder"
) 
#start date
with col1:
    start_date=st.date_input("Input strating date", datetime.date(2020,1,1))
with col2:
    end_date = st.date_input("Input end date", datetime.date(2025,1,31))
ticker_data = yf.Ticker(ticker_symbol)
ticker_df = ticker_data.history(start=start_date, end=end_date
                                ,interval = "1d")
st.write(f"""
    ## {ticker_symbol}"s EOD Prices
    """
)
st.dataframe(ticker_df)
st.write(
    
    """
   # Daily closing chart
    """
)
st.line_chart(ticker_df.Close)


st.write(
    
    """
   # Daily Volume chart 
    """
)
st.line_chart(ticker_df.Volume)