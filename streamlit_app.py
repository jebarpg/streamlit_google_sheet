# Import dependencies
import streamlit as st
import pandas as pd
from streamlit_gsheets import GSheetsConnection

# Create a connection object
url = "https://docs.google.com/spreadsheets/d/1pZkq7l2JPEmIePg8acAD_rPM0FHXwp6p54hTjp530K4/edit?usp=sharing"
conn = st.connection("gsheets", type=GSheetsConnection)
data = conn.read(spreadsheet=url)
st.dataframe(data)