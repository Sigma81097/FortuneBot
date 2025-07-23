import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="FortuneBot - Crypto Portfolio Dashboard", layout="wide")
st.title("💰 FortuneBot: AI-Powered Crypto Portfolio Dashboard")

uploaded_file = st.file_uploader("📂 Upload your CoinDCX Portfolio CSV", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    st.subheader("📊 Portfolio Summary")
    st.dataframe(df.style.format({
        "Invested Amount (₹)": "₹{:.2f}",
        "Current Price (₹)": "₹{:.4f}",
        "Profit/Loss (₹)": "₹{:.2f}",
        "% Change": "{:.2f}%",
        "Portfolio Weight %": "{:.2f}%"
    }), use_container_width=True)

    st.markdown("---")
    
    st.subheader("📈 Portfolio Breakdown by Coin")
    pie = px.pie(df, values='Portfolio Weight %', names='Coin', title='Holdings Allocation')
    st.plotly_chart(pie, use_container_width=True)

    st.subheader("📉 Profit/Loss Overview")
    bar = px.bar(df, x='Coin', y='Profit/Loss (₹)', color='Profit/Loss (₹)',
                 color_continuous_scale='RdYlGn', title='Profit/Loss per Coin')
    st.plotly_chart(bar, use_container_width=True)

    st.markdown("---")
    st.subheader("📌 Buy/Sell Suggestions")
    suggestions = df[['Coin', 'Buy Recommendation', 'AI Fortune Score', 'Sentiment Summary']]
    st.dataframe(suggestions, use_container_width=True)

else:
    st.info("👆 Please upload your CoinDCX portfolio CSV to view insights.")
