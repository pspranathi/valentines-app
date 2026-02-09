import streamlit as st
import random

st.set_page_config(page_title="Valentine's Surprise", layout="centered")

# Romantic gradient background
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

/* Falling hearts animation */
@keyframes fall {
  0% {transform: translateY(-10%);}
  100% {transform: translateY(110%);}
}
.heart {
  position: fixed;
  top: -10%;
  font-size: 30px;
  color: red;
  animation: fall linear infinite;
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# Title
st.markdown("<h1 style='text-align:center; color:red;'>💝 Happy Valentine's Day 💝</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align:center; color:purple;'>Forever Yours ❤️</h2>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align:center; color:darkred;'>Will you be my Valentine?</h3>", unsafe_allow_html=True)

# Dramatic sentences for "No"
dramatic_lines = [
    "💔 Oh no... my heart is breaking!",
    "😢 How could you say no to me?",
    "🌹 Without you, Valentine's loses its meaning...",
    "💕 Please... say YES, my love!"
]

# Buttons
col1, col2 = st.columns(2)
with col1:
    if st.button("Yes 💕"):
        st.success("💖 Yay! You said YES! 💖 🎉")
        # Scatter hearts across the whole screen
        hearts_html = "".join(
            [
                f"<div class='heart' style='left:{random.randint(0,95)}%; animation-duration:{random.randint(3,6)}s; animation-delay:{random.uniform(0,2)}s;'>❤️</div>"
                for _ in range(20)
            ]
        )
        st.markdown(hearts_html, unsafe_allow_html=True)

with col2:
    if st.button("No 💔"):
        st.warning(random.choice(dramatic_lines))
