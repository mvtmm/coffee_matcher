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
st.write("Click the button below to spin the wheel and get matched with a random colleague!")

# List of colleagues
colleague_list = ["Alice", "Bob", "Charlie", "Dave", "Eve", "Frank", "Grace", "Hannah", "Ivy", "Jack"]

# Add HTML for the wheel
st.markdown("""
    <div id="wheel" style="width: 200px; height: 200px; border: 16px solid #f3f3f3; border-top: 16px solid #3498db; border-radius: 50%; position: relative;">
      <div id="pointer" style="width: 50%; height: 4px; background-color: red; position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%) rotate(90deg);"></div>
    </div>
    <script>
      setTimeout(function() {
        var wheel = document.getElementById("wheel");
        wheel.style.transition = "transform 5s ease-out";
        wheel.style.transform = "rotate(" + (360 * 5) + "deg)";
      }, 1000);
    </script>
""", unsafe_allow_html=True)

# Button to get a random colleague
if st.button('Spin the Wheel!'):
    # Here you can call your Python function to get a random colleague
    matched_colleague = get_random_colleague(colleague_list)
    # And then display the matched colleague. 
    st.success(f"You've been matched with {matched_colleague}!")
