import streamlit as st
import pandas as pd
import openpyxl

st.set_page_config(
    page_title="Temperstura",
    page_icon = "🌡",
    layout= "wide"
)

if "date" not in st.session_state:
    df_temp = pd.read_excel("temperatura.xlsx")
    st.session_state["date"] = df_temp
    
df_temp = st.session_state["date"]

df_temp
    
