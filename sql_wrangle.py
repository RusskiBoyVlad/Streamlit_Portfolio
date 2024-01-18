
# %%
import pandas as pd 
import streamlit as st
import random
# %%
import sys
print(sys.path)
#%%

def generate_random_number():
    return random.randint(1, 100)

def main():
    st.title("Simple Streamlit Application")

    # Add a button to generate and display a random number
    if st.button("Generate Random Number"):
        random_number = generate_random_number()
        st.success(f"Random Number: {random_number}")

if __name__ == "__main__":
    main()