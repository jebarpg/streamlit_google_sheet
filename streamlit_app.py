# Import dependencies
import streamlit as st
import pandas as pd
from streamlit_gsheets import GSheetsConnection

# Create a connection object
conn = st.connection("gsheets", type=GSheetsConnection)
url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTPg2ynowaOy_4G6R9BMIwZd6M9RudnYXOAZhQMmJ8xL8l-SklGybTpquoA4ZaCNgPQT3Is16W782UJ/pubhtml?gid=0&amp;single=true&amp;widget=true&amp;headers=false"
google_sheets_table = conn.read(spreadsheet=url)
dataframe = pd.DataFrame(google_sheets_table) # Convert google sheets table into python dataframe. Streamlit expects dataframes as input.

# Introduction text
"""
Hi there! This is a simple Google Sheets example on how to embed a dynamic table on a Medium blog post with Streamlit! 
"""

# Define tabs
tab1 = st.tabs(["Sheet1"])

# Streamlit content
with tab1:
  st.write(dataframe)

# Footer text
"""
The data shown above is the historic stock price of Google. In the "Graph" tab I have put an example of a simple graph that can be embedded. 
"""
"""
You can read my blog here: https://medium.com/@steffenjanbrouwer/how-to-embed-data-tables-and-graphs-in-your-medium-blogs-16d93d99ebc7
"""
