import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="📈 Global Tech Stock Dashboard",
    page_icon="📊",
    layout="wide"
)

st.markdown("""
<style>

.stApp{
background:
linear-gradient(
180deg,
#f8fbff,
#f4f7ff,
#ffffff
);
}

.metric{
padding:18px;
border-radius:20px;
background:white;
box-shadow:0 6px 20px rgba(0,0,0,0.06);
}

.big{
font-size:42px;
font-weight:800;
}

.small{
color:#666;
}

</style>
""",
unsafe_allow_html=True
)

stocks = {
    "삼성전자":"005930.KS",
    "SK하이닉스":"000660.KS",
    "구글":"GOOGL",
    "마이크로소프트":"MSFT",
    "애플":"AAPL"
}

st.markdown(
"""
<div class='big'>
📈 최근 1년 주가 비교 분석
</div>

<div class='small'>
삼성전자 · SK하이닉스 · 구글 · Microsoft · Apple
</div>
""",
unsafe_allow_html=True
)

@st.cache_data
def load_data():

    raw = yf.download(
        list(stocks.values()),
        period="1y",
        auto_adjust=True,
        progress=False
    )

    close = raw["Close"]

    close.columns = list(stocks.keys())

    close = close.dropna()

    return close

try:

    data = load_data()

    normalized = (
        data /
        data.iloc[0]
    ) * 100

    fig = px.line(
        normalized,
        x=normalized.index,
        y=normalized.columns,
        title="최근 1년 누적 주가 변화 (시작=100)"
    )

    fig.update_layout(
        height=700,
        hovermode="x unified",
        legend_title="기업",
        template="plotly_white"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.subheader("📌 핵심 요약")

    cols = st.columns(5)

    for idx, company in enumerate(data.columns):

        latest = data[company].iloc[-1]

        change = (
            (
                latest
                /
                data[company].iloc[0]
            ) - 1
        ) * 100

        with cols[idx]:

            st.metric(
                company,
                f"{latest:,.0f}",
                f"{change:+.1f}%"
            )

    st.markdown("---")

    winner = (
        (
            data.iloc[-1]
            /
            data.iloc[0]
            - 1
        )
        .idxmax()
    )

    loser = (
        (
            data.iloc[-1]
            /
            data.iloc[0]
            - 1
        )
        .idxmin()
    )

    st.subheader("🧠 자동 분석")

    st.write(
        f"""
📈 최근 1년 기준 가장 상승폭이 큰 종목: **{winner}**

📉 상대적으로 수익률이 낮은 종목: **{loser}**

💡 그래프에서 확대·축소·범례 클릭으로 종목별 비교 가능
"""
    )

except Exception as e:

    st.error(
        "데이터를 불러오지 못했어요 😢"
    )

    st.code(str(e))
streamlit
yfinance
pandas
plotly
