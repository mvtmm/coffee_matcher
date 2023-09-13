# Import Streamlit
import streamlit as st
# Import random for random selection
import random

# Function to get a random colleague
def get_random_colleague(colleague_list):
    return random.choice(colleague_list)

# Title of the application
st.title('Random Colleague Matcher')

# Instructions
st.write("Click the button below to get matched with a random colleague!")

# List of colleagues
colleague_list = ["Alice", "Bob", "Charlie", "Dave", "Eve", "Frank", "Grace", "Hannah", "Ivy", "Jack"]

# Button to get a random colleague
if st.button('Match Me!'):
    matched_colleague = get_random_colleague(colleague_list)
    st.success(f"You've been matched with {matched_colleague}!")
