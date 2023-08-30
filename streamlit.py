import streamlit as st

#functions to be defined:
def print_recommendation(text):
    pass

#Here below is the code to define the side bar

st.sidebar.text('\n\n\n')
st.sidebar.markdown("**Select the wine in your mind:** 👇")
st.sidebar.write("No, no wine over 150 euro.")
st.sidebar.slider('Price range',0.0, 150.0, (10.0, 50.0))

#Here below is the code to define the main page
st.title("Find the wine you like!")