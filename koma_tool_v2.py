import streamlit as st

st.set_page_config(page_title="モヤっと言葉から考えるツール", page_icon="💬", layout="centered")

st.markdown("""
    <style>
    body {
        background-color: #FFF7F0;
        font-family: "メイリオ", sans-serif;
    }
    .title {
        color: #B65C3A;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
# 💬 モヤっと言葉から考えるツール

言われてつらかった、モヤっとした言葉。<br>
その気持ちを否定せず、自分の中で整理し、少しだけ前を向けるように。

気になる言葉をひとつ選んでみてください。
""", unsafe_allow_html=True)

options = {
    "気にしすぎじゃない？": {
        "feeling": "わたしなりにちゃんと考えて行動してるのに、それを軽く扱われた気がしたのかもしれません。",
        "background": [
            "不安を減らすために丁寧に準備するタイプかもしれません。",
            "曖昧なことが苦手で、できるだけ明確にしたい気持ちが強いのかも。",
            "過去に『神経質』などと評価されて、傷ついた経験があるのかもしれません。"
        ],
        "advice": [
            "あなたが“気にしてる”ことは、きっと大切にしている価値でもあります。",
            "“気にしすぎ”と言われたときは、会話の温度差があるサインとして受け取ってもいいかもしれません。",
            "相手に合わせることより、自分の感覚を大事にしていくことも、立派な選択です。"
        ]
    }
}

choice = st.selectbox("選んでください：", list(options.keys()))

if choice:
    data = options[choice]
    st.markdown(f"### 🗯️ 言葉：『{choice}』")
    st.markdown(f"**💬 モヤっとした理由：** {data['feeling']}")

    st.markdown("**🧠 背景にあるかもしれないこと：**")
    for bg in data['background']:
        st.markdown(f"- {bg}")

    st.markdown("**🌱 とらえ方のヒント：**")
    for tip in data['advice']:
        st.markdown(f"- {tip}")
