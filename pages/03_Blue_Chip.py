import streamlit as st
from datetime import date
import pandas as pd
import plotly.express as px
import numpy as np

st.title(body = "Blue Chip")
st.caption(body = date.today())
st.markdown(body = "* Horizontal Axis - MC (Million)")
st.markdown(body = "* Text - FV (%)")
st.markdown(body = "* Vertical Axis - Ticker")

with st.expander("How to interpret the chart?"):
    st.markdown("""
    This chart helps investors and traders identify stocks with a cheap valuation and a high liquidity.
    """)

if "col" in st.session_state:
    
    # Import Data
    
    col = st.session_state["col"]
    col_notna = col[col["Fundamental Rating"].notna()]
    df = col_notna
    df = df.reset_index()
    
    bar = df.sort_values(by = "MC (Billion)", ascending = True)
    
    # Color
    
    color = st.selectbox(label = "Color", options = [None, "Sector", "Subsector"])
    
    # Custom Data
    
    custom_data = ["Ticker"] + ["Sector", "Subsector", "MC (Billion)", "P", "FV", "FV (%)"]
    
    # Plot Data
    
    hovertemplate = "<br>".join(["<b>%{customdata[0]}</b>"] + ["<b>" + str(custom_data[i]) + ":</b> %{customdata[" + str(i) + "]}" for i in range(1, len(custom_data))])
    
    fig = px.bar(data_frame = bar,
                 x = "MC (Billion)",
                 y = "Ticker",
                 color = color,
                 custom_data = custom_data,
                 text = "FV (%)",
                 width = 1000,
                 height = 1000)
    
    fig.update_traces(hovertemplate = hovertemplate, textposition = "outside")
    
    st.plotly_chart(figure_or_data = fig, use_container_width = True)
