import streamlit as st

# Title of the app
st.title("🚀 My First Streamlit App")

# A simple text message
st.write("Hello, world! 👋")

# Text input
name = st.text_input("What's your name?")

# Button + output
if st.button("Greet me"):
    st.success(f"Nice to meet you, {name}!")
