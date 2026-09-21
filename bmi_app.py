import pandas as pd
import numpy as np
import plotly.express as px
import streamlit as st

st.markdown("""
<style>
body {
    background-color: #f8f9fa;
    font-family: "Prompt", sans-serif;
}
</style>
""", unsafe_allow_html=True)


# Give a title to the app
st.title('Welcome to BMI Calculator')

if "person_df" not in st.session_state:
    st.session_state.person_df = pd.DataFrame({
        "weigth":[],
        "height":[],
        "unit":[],
        "bmi":[],
        "category":[]
    })

with st.form("bmi_from", clear_on_submit=True):

    # Take weight input in kgs
    weight = st.number_input("Enter your weight (in kgs)")

    # Radio button to choose height format
    status = st.radio('Select your height format: ', ('cms', 'meters', 'feet'))

    # Initialize bmi variable
    bmi = None

    # Compare status value to take the appropriate height input
    if status == 'cms':
        height = st.number_input('Centimeters')
        try:
            bmi = weight / ((height / 100) ** 2)
        except ZeroDivisionError:
            st.text("Enter a valid value for height")
    elif status == 'meters':
        height = st.number_input('Meters')
        try:
            bmi = weight / (height ** 2)
        except ZeroDivisionError:
            st.text("Enter a valid value for height")
    else:
        height = st.number_input('Feet')
        try:
            bmi = weight / ((height / 3.28) ** 2)
        except ZeroDivisionError:
            st.text("Enter a valid value for height")
            
    summitBtn = st.form_submit_button('Calculate BMI')

    # Check if the 'Calculate BMI' button is pressed
    if summitBtn:
        category = ""
        
        if bmi is not None:
            st.text("Your BMI Index is {:.2f}.".format(bmi))
            
            if bmi < 16:
                st.error("You are Extremely Underweight")
                category = "Extremely Underweight"
                
            elif 16 <= bmi < 18.5:
                st.warning("You are Underweight")
                category = "Underweight"
            elif 18.5 <= bmi < 25:
                st.success("Healthy")
                category = "Healthy"
            elif 25 <= bmi < 30:
                st.warning("Overweight")
                category = "Overweight"
            elif bmi >= 30:
                st.error("Extremely Overweight")
                category = "Extremely Overweight"
            
            
            person_info = pd.DataFrame({
                "weigth":[weight],
                "height":[height],
                "unit":[status],
                "bmi":[bmi],
                "category":[category]
            })
            
            st.session_state.person_df = pd.concat(
                [st.session_state.person_df, person_info],
                ignore_index=True
            )            
        else:
            st.error("Please enter valid weight and height to calculate BMI.")
        
st.header("BMI Records")

if not st.session_state.person_df.empty:
    st.dataframe(
        st.session_state.person_df,
        use_container_width=True, # ปรับความกว้างให้ยืดเต็มจออัตโนมัติ
        hide_index=True
    )
else:
    st.info("No person data available yet. Please add data above.")