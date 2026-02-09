import streamlit as st
import random

st.set_page_config(page_title="Valentine's Surprise", layout="centered")

# Romantic gradient background + styles
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

/* Glowing pulse for love message */
@keyframes glow {
  0% { text-shadow: 0 0 5px red, 0 0 10px pink; }
  50% { text-shadow: 0 0 20px hotpink, 0 0 30px red; }
  100% { text-shadow: 0 0 5px red, 0 0 10px pink; }
}
.glow-text {
  color: red;
  text-align: center;
  font-size: 2em;
  animation: glow 2s infinite;
}

/* Centered heart button */
.center-button {
  display: flex;
  justify-content: center;
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# --- Intro Screen ---
if "started" not in st.session_state:
    st.markdown("<h2 style='text-align:center; color:darkred;'>To the man who supports my dreams and fills my heart:</h2>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align:center; color:red;'>💝 Happy early Valentine’s Day 💝</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align:center; color:purple;'>Click the heart below to continue...</h3>", unsafe_allow_html=True)

    # Centered heart button
    col = st.columns([1,2,1])  # empty columns on sides, button in middle
    with col[1]:
        if st.button("❤️"):
            st.session_state.started = True
    st.stop()

# --- Main Valentine Question ---
st.markdown("<h1 style='text-align:center; color:red;'>💝 Happy Valentine's Day 💝</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align:center; color:purple;'>Forever Yours ❤️</h2>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align:center; color:darkred;'>Will you be my Valentine?</h3>", unsafe_allow_html=True)

dramatic_lines = [
    "💔 Oh no... my heart is breaking!",
    "😢 How could you say no to me?",
    "🌹 Without you, Valentine's loses its meaning...",
    "💫 Destiny insists... you must be mine!",
    "💕 Please... say YES, my love!"
]

col1, col2 = st.columns(2)
with col1:
    if st.button("Yes 💕"):
        st.success("💖 Yay! You said YES! 💖 🎉 Balloons burst! 🎈 Confetti everywhere! 💕")
        st.markdown("<div class='glow-text'>I love you Suraj Pamadi ❤️</div>", unsafe_allow_html=True)

        # Falling hearts across the screen
        hearts_html = "".join(
            [
                f"<div class='heart' style='left:{random.randint(0,95)}%; animation-duration:{random.randint(3,6)}s; animation-delay:{random.uniform(0,2)}s;'>❤️</div>"
                for _ in range(30)
            ]
        )
        st.markdown(hearts_html, unsafe_allow_html=True)

with col2:
    if st.button("No 💔"):
        st.warning(random.choice(dramatic_lines))
