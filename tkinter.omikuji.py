import streamlit as st
import random
import os

st.title("🧙‍♂️ 手作りおみくじアプリ")

dir_path = os.path.dirname(__file__)
if st.button("占う", type="primary"):
    kujis = ["daikichi.png", "chukichi.png", "kichi.png", "kyo.png"]
    result_img = random.choice(kujis)
    img_path = os.path.join(dir_path, result_img)
    st.image(img_path, width=300)
else:
    empty_path = os.path.join(dir_path, "empty.png")
    st.image(empty_path, width=300)
