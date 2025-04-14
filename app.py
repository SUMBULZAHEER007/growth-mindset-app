import streamlit as st
import random

# Title
st.title("🌱 Growth Mindset Challenge")

# List of growth mindset challenges
challenges = [
    "Try something new that scares you a little.",
    "Reflect on a recent failure and what you learned.",
    "Help someone else learn something new.",
    "Spend 10 minutes journaling your goals.",
    "Take a short break and come back with a fresh perspective.",
    "Ask for feedback on something you created.",
    "Learn about a topic you’ve never explored before."
]

# Button to show a random challenge
if st.button("Give me a challenge!"):
    st.success(random.choice(challenges))
