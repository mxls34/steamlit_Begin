import pandas as pd
import numpy as np
import plotly.express as px
import streamlit as st

home_page = st.Page("home.py", title="app")
register_page = st.Page("register.py", title="Register")
login_page = st.Page("login.py", title="Login")

nav = st.navigation([home_page, register_page, login_page])

nav.run()