import streamlit as st
import yfinance as yf
import plotly.express as px

st.set_page_config(
    page_title="Market Leaders",
    layout="wide"
)

st.markdown("""
<style>

.stApp{
background:
linear-gradient(
180deg,
#f5f7fb,
#ffffff
);
}

.header{
background:white;
padding:28px;
border-radius:18px;
box-shadow:0 6px 24px rgba(0,0,0,.05);
}

.title{
font-size:44px;
font-weight:800;
}

.sub{
color:#777;
}

</style>
""",
unsafe_allow_html=True)

stocks = {

"Apple":"AAPL",
"Microsoft":"MSFT",
"Tesla":"TSLA",
"NVIDIA":"NVDA",
"Amazon":"AMZN",

"Alphabet":"GOOGL",
"Meta":"META",
"Samsung":"005930.KS",
"SK hynix":"000660.KS",
"Netflix":"NFLX"

}


@st.cache_data
def load():

    raw = yf.download(
        list(stocks.values()),
        period="1y",
        auto_adjust=True,
        progress=False
    )

    close = raw["Close"]

    close.columns = list(
        stocks.keys()
    )

    return close.dropna()


st.markdown("""
<div class="header">

<div class="title">
Market Leaders Dashboard
</div>

<div class="sub">
Top 10 Global Stocks · 1 Year Performance
</div>

</div>
""",
unsafe_allow_html=True)

data = load()

normalized = (
    data
    /
    data.iloc[0]
) * 100

st.markdown("## Performance Comparison")

fig = px.line(
    normalized,
    x=normalized.index,
    y=normalized.columns
)

fig.update_layout(

height=720,

template="plotly_white",

hovermode="x unified",

legend_title="Stocks",

margin=dict(
l=20,
r=20,
t=30,
b=20
)

)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.markdown("## Market Snapshot")

cols = st.columns(5)

returns = (
    data.iloc[-1]
    /
    data.iloc[0]
    - 1
) * 100

latest = data.iloc[-1]

companies = list(
    data.columns
)

for i in range(10):

    with cols[i % 5]:

        st.metric(
            companies[i],
            f"{latest.iloc[i]:,.0f}",
            f"{returns.iloc[i]:+.1f}%"
        )

st.markdown("---")

best = returns.idxmax()

worst = returns.idxmin()

c1, c2 = st.columns(2)

with c1:

    st.markdown(
f"""
### Best Performer

{best}

Return:
{returns[best]:.2f}%
"""
)

with c2:

    st.markdown(
f"""
### Lowest Performer

{worst}

Return:
{returns[worst]:.2f}%
"""
)

st.markdown("## Recent Data")

st.dataframe(
    data.tail(30),
    use_container_width=True
)
