# Import dependencies
import streamlit as st
import pandas as pd
from streamlit_gsheets import GSheetsConnection

# Create a connection object
url = "https://docs.google.com/spreadsheets/d/1pZkq7l2JPEmIePg8acAD_rPM0FHXwp6p54hTjp530K4/edit?usp=sharing"
conn = st.experimental_connection("gsheets", type=GSheetsConnection)
data = conn.read(spreadsheet=url)
st.dataframe(data)

# Introduction text
"""
Hi there! This is a simple Google Sheets example on how to embed a dynamic table on a Medium blog post with Streamlit! 
"""


# Footer text
"""
The data shown above is the historic stock price of Google. In the "Graph" tab I have put an example of a simple graph that can be embedded. 
"""
"""
You can read my blog here: https://medium.com/@steffenjanbrouwer/how-to-embed-data-tables-and-graphs-in-your-medium-blogs-16d93d99ebc7
"""