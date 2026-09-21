import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Define the pages
main_page = st.Page("app.py", title="Main Page", icon="🎈")
df_page = st.Page("formtoDF.py", title="DataFrame", icon="❄️")
plotly_page= st.Page("plotly_filter_app.py", title="Plotly", icon="🎉")

# Set up navigation
pg = st.navigation([main_page, df_page, plotly_page])

# Run the selected page
pg.run()