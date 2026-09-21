import pandas as pd
import numpy as np
import plotly.express as px
import streamlit as st

st.title(":memo: Register Page")

st.text("Create your student account.")

# input
st.text_input("Full Name", key="full_name")
st.number_input("Student ID", key="student_id")

