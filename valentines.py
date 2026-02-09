import streamlit as st
import random

st.set_page_config(page_title="Valentine's Surprise", layout="centered")

st.markdown("<h1 style='text-align:center; color:red;'>💝 Happy Valentine's Day 💝</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align:center;'>Forever Yours ❤️</h2>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align:center;'>Will you be my Valentine?</h3>", unsafe_allow_html=True)

# Dramatic sentences for "No"
dramatic_lines = [
    "💔 Oh no... my heart is breaking!",
    "😢 How could you say no to me?",
    "🌹 Without you, Valentine's loses its meaning...",
    "💕 Please... say YES, my love!"
]

if st.button("Yes 💕"):
    st.success("💖 Yay! You said YES! 💖 🎉 Balloons burst! 🎈 Confetti everywhere! 💕")
elif st.button("No 💔"):
    st.warning(random.choice(dramatic_lines))
