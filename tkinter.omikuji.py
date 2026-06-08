import streamlit as st
import random
import os

st.title("🧙‍♂️ 手作りおみくじアプリ")

# このプログラムがある場所を調べる
dir_path = os.path.dirname(__file__)

# ボタンが押されたらおみくじを引く
if st.button("占う", type="primary"):
kujis = ["daikichi.png", "chukichi.png", "kichi.png", "kyo.png"]
result_img = random.choice(kujis)

# 画像の場所をドッキング
img_path = os.path.join(dir_path, result_img)
st.image(img_path, width=300)
else:
# まだボタンを押していない時は empty.png を出す
empty_path = os.path.join(dir_path, "empty.png")
st.image(empty_path, width=300)
