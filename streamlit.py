import streamlit as st

#Here below is the code to define the side bar

st.sidebar.text('\n\n\n')
st.sidebar.markdown("**Select the wine in your mind:** 👇")
st.sidebar.write("No, no wine over 150 euro.")
st.sidebar.slider('Price range',0.0, 150.0, (10.0, 50.0))

#Here below is the code to define the main page
st.markdown("##Your recommondation will be below once you submit")
# age = st.slider('How old are you?', 0, 130, 25)
# st.write("I'm ", age, 'years old')

# values = st.slider(
#     'Select a range of values',
#     0.0, 100.0, (25.0, 75.0))
# st.write('Values:', values)