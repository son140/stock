import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Stock Performance Dashboard",
    layout="wide"
)

st.markdown("""
<style>

.stApp{
background:#f7f9fc;
}

.block{
background:white;
padding:24px;
border-radius:16px;
box-shadow:0 4px 18px rgba(0,0,0,.05);
}

.title{
font-size:40px;
font-weight:700;
}

.subtitle{
color:#666;
}

</style>
""",
unsafe_allow_html=True)

stocks = {
    "Samsung Electronics":"005930.KS",
    "SK hynix":"000660.KS",
    "Alphabet":"GOOGL",
    "Microsoft":"MSFT",
    "Apple":"AAPL"
}


@st.cache_data
def load():

    data = yf.download(
        list(stocks.values()),
        period="1y",
        auto_adjust=True,
        progress=False
    )

    close = data["Close"]

    close.columns = list(stocks.keys())

    close = close.dropna()

    return close


st.markdown("""
<div class="block">

<div class="title">
Stock Performance Dashboard
</div>

<div class="subtitle">
1-Year Comparative Analysis
</div>

</div>
""",
unsafe_allow_html=True)

try:

    prices = load()

    returns = (
        prices
        /
        prices.iloc[0]
    ) * 100

    st.markdown("### Price Performance")

    fig = px.line(
        returns,
        x=returns.index,
        y=returns.columns
    )

    fig.update_layout(
        template="plotly_white",
        height=650,
        hovermode="x unified",
        legend_title="Company",
        margin=dict(
            l=30,
            r=30,
            t=30,
            b=30
        )
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.markdown("### Key Metrics")

    cols = st.columns(5)

    total = (
        prices.iloc[-1]
        /
        prices.iloc[0]
        - 1
    ) * 100

    latest = prices.iloc[-1]

    for i, company in enumerate(prices.columns):

        with cols[i]:

            st.metric(
                label=company,
                value=f"{latest[company]:,.0f}",
                delta=f"{total[company]:+.2f}%"
            )

    st.markdown("---")

    st.markdown("### Summary")

    best = total.idxmax()
    worst = total.idxmin()

    c1, c2 = st.columns(2)

    with c1:

        st.info(
f"""
Best Performer

{best}

Return:
{total[best]:.2f}%
"""
)

    with c2:

        st.info(
f"""
Lowest Performer

{worst}

Return:
{total[worst]:.2f}%
"""
)

    st.markdown("### Raw Data")

    st.dataframe(
        prices.tail(20),
        use_container_width=True
    )

except Exception as e:

    st.error(
        "Failed to load stock data."
    )

    st.code(str(e))
