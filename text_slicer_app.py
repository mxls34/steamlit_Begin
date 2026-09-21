import numpy as np
import pandas as pd
import streamlit as st 

st.header(":red[Selection]") 
status = st.radio("Select Gender: ", ('Male', 'Female'))
if (status == 'Male'): st.success("Male")
else: st.success("Female")

#selction box
hobby = st.selectbox("Hobbies: ", ['Dancing', 'Reading', 'Sports'])
st.write("Your hobby is: ", hobby)

#multi selection
hobbies = st.multiselect("Hobbies: ", ['Dancing', 'Reading', 'Sports'])
st.write("You selected", len(hobbies), 'hobbies')

#button
st.button("Click me for no reason")
if(st.button("About")):
     st.text("Welcome To Machine Learning!!!")

#-----------------------------------Input Text------------------------------
st.header(":green[Input text]")
name = st.text_input("Enter Your name", "Type Here ...")

result = ""   #Initialize result variable
if st.button('Submit'):
   result = name.title()
   st.success(result) # Now result is always defined

#-----------------------------------Slicing---------------------------------

st.header(":rainbow[Slicer]")
level = st.slider("Select the level", 1, 5) 
st.text('Selected: {}'.format(level))
