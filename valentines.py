import streamlit as st
import random

st.set_page_config(page_title="Valentine's Surprise", layout="centered")

# --- Intro Screen ---
if "started" not in st.session_state:
    st.markdown("<h2 style='text-align:center; color:darkred;'>To the man who supports my dreams and fills my heart:</h2>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align:center; color:red;'>💝 Happy early Valentine’s Day 💝</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align:center; color:purple;'>Click the heart below to continue...</h3>", unsafe_allow_html=True)

    col = st.columns([1,2,1])
    with col[1]:
        if st.button("❤️"):
            st.session_state.started = True
    st.stop()

# --- Valentine Question Page ---
if "started" in st.session_state and "yes_clicked" not in st.session_state:
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
            st.session_state.yes_clicked = True
    with col2:
        if st.button("No 💔"):
            st.warning(random.choice(dramatic_lines))

# --- Final Neon Love Page ---
if "yes_clicked" in st.session_state:
    neon_page = """
    <style>
    [data-testid="stAppViewContainer"] {
        background-color: black;
    }
    @keyframes neon {
      0% { text-shadow: 0 0 5px #ff0000, 0 0 10px #ff66cc, 0 0 20px #ff3399; color: #ff0066; }
      25% { text-shadow: 0 0 5px #00ffff, 0 0 10px #66ffff, 0 0 20px #33ccff; color: #00ccff; }
      50% { text-shadow: 0 0 5px #00ff00, 0 0 10px #66ff66, 0 0 20px #33cc33; color: #00ff99; }
      75% { text-shadow: 0 0 5px #ffff00, 0 0 10px #ffcc00, 0 0 20px #ff9933; color: #ffcc00; }
      100% { text-shadow: 0 0 5px #ff0000, 0 0 10px #ff66cc, 0 0 20px #ff3399; color: #ff0066; }
    }
    .neon-text {
      text-align: center;
      font-size: 3em;
      font-family: "Brush Script MT", cursive;
      animation: neon 3s infinite;
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
      animation: fall linear infinite;
    }
    </style>
    """
    st.markdown(neon_page, unsafe_allow_html=True)

    # Neon love text
    st.markdown("<div class='neon-text'>I LOVE YOU SURAJ PAMADI ❤️</div>", unsafe_allow_html=True)

    # Falling hearts across the screen
    hearts_html = "".join(
        [
            f"<div class='heart' style='left:{random.randint(0,95)}%; color:red; animation-duration:{random.randint(3,6)}s; animation-delay:{random.uniform(0,2)}s;'>❤️</div>"
            for _ in range(40)
        ]
    )
    st.markdown(hearts_html, unsafe_allow_html=True)
