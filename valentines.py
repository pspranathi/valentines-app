import streamlit as st
import random

# Page setup
st.set_page_config(page_title="Valentine's Surprise", layout="centered")

# Romantic background using CSS
page_bg = """
<style>
[data-testid="stAppViewContainer"] {
    background-image: linear-gradient(to bottom right, pink, lavender, mistyrose);
    background-size: cover;
}
[data-testid="stHeader"] {
    background: rgba(0,0,0,0);
}
[data-testid="stToolbar"] {
    right: 2rem;
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# Title and subtitle
st.markdown("<h1 style='text-align:center; color:red;'>💝 Happy Valentine's Day 💝</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align:center; color:purple;'>Forever Yours ❤️</h2>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align:center; color:darkred;'>Will you be my Valentine?</h3>", unsafe_allow_html=True)

# Dramatic sentences for "No"
dramatic_lines = [
    "💔 Oh no... my heart is breaking!",
    "😢 How could you say no to me?",
    "🌹 Without you, Valentine's loses its meaning...",
    "💫 Destiny insists... you must be mine!",
    "💕 Please... say YES, my love!"
]

# Buttons
col1, col2 = st.columns(2)
with col1:
    if st.button("Yes 💕"):
        st.success("💖 Yay! You said YES! 💖 🎉 Balloons burst! 🎈 Confetti everywhere! 💕")
with col2:
    if st.button("No 💔"):
        st.warning(random.choice(dramatic_lines))
