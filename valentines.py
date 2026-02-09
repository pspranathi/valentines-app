import streamlit as st
import random

st.set_page_config(page_title="Valentine's Surprise", layout="centered")

# --- Shared romantic background for first 2 pages ---
romantic_bg = """
<style>
[data-testid="stAppViewContainer"] {
    background-image: linear-gradient(to bottom right, pink, lavender, mistyrose);
    background-size: cover;
}
[data-testid="stHeader"], [data-testid="stToolbar"] {
    background: rgba(0,0,0,0);
}
</style>
"""

# --- Intro Screen ---
if "started" not in st.session_state:
    st.markdown(romantic_bg, unsafe_allow_html=True)
    st.markdown("<h2 style='text-align:center; color:darkred;'>To the man who supports my dreams and fills my heart:</h2>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align:center; color:red;'>💝 Happy early Valentine’s Day 💝</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align:center; color:purple;'>Click the heart below to continue...</h3>", unsafe_allow_html=True)

    # Centered heart button (single click works with unique key)
    col = st.columns([1,2,1])
    with col[1]:
        if st.button("❤️", key="start_button"):
            st.session_state.started = True
    st.stop()

# --- Valentine Question Page ---
if "started" in st.session_state and "yes_clicked" not in st.session_state:
    st.markdown(romantic_bg, unsafe_allow_html=True)
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
        if st.button("Yes 💕", key="yes_button"):
            st.session_state.yes_clicked = True
            st.stop()   # stop here so next run shows final page
    with col2:
        if st.button("No 💔", key="no_button"):
            st.warning(random.choice(dramatic_lines))

# --- Final Love Page ---
if "yes_clicked" in st.session_state:
    final_page = """
    <style>
    [data-testid="stAppViewContainer"] {
        background-color: black;
    }
    @keyframes fadein {
      from {opacity: 0;}
      to {opacity: 1;}
    }
    .love-text {
      text-align: center;
      font-size: 3em;
      font-family: Verdana, Geneva, sans-serif;
      color: limegreen;
      margin-top: 40vh; /* centers vertically */
      animation: fadein 3s ease-in;
    }
    @keyframes fall {
      0% {transform: translateY(-10%);}
      100% {transform: translateY(110%);}
    }
    .heart {
      position: fixed;
      top: -10%;
      font-size: 30px;
      animation: fall linear infinite;
    }
    </style>
    """
    st.markdown(final_page, unsafe_allow_html=True)

    # Centered green love text with fade-in
    st.markdown("<div class='love-text'>I LOVE YOU SURAJ PAMADI ❤️</div>", unsafe_allow_html=True)

    # Falling hearts
    hearts_html = "".join(
        [
            f"<div class='heart' style='left:{random.randint(0,95)}%; color:red; animation-duration:{random.randint(3,6)}s; animation-delay:{random.uniform(0,2)}s;'>❤️</div>"
            for _ in range(40)
        ]
    )
    st.markdown(hearts_html, unsafe_allow_html=True)
