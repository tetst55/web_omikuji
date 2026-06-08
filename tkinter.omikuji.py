import streamlit as st
import random
import os

st.title("🧙‍♂️ 手作りおみくじアプリ")

dir_path = os.path.dirname(__file__)

# 画面の状態を記憶しておくおまじない
if "kuji_result" not in st.session_state:
    st.session_state.kuji_result = "empty.png"

# 横並びのボタンを作る
col1, col2 = st.columns(2)

with col1:
    if st.button("占う", type="primary"):
        kujis = ["daikichi.png", "chukichi.png", "kichi.png", "kyo.png"]
        st.session_state.kuji_result = random.choice(kujis)

with col2:
    if st.button("クリア"):
        st.session_state.kuji_result = "empty.png"

# 画像を表示する
img_path = os.path.join(dir_path, st.session_state.kuji_result)
st.image(img_path, width=300)
