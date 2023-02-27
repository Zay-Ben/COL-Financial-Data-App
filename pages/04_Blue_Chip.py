import streamlit as st
from datetime import date
import pandas as pd
import plotly.express as px
import numpy as np
import customdata_hovertemplate

st.title(body = "Blue Chip")

st.caption(body = date.today())

st.markdown(body = "* Horizontal Axis - MC (Million)")
st.markdown(body = "* Vertical Axis - Ticker")
st.markdown(body = "* Text - FV (%)")

if "col" in st.session_state:
    
    # Import Data
    
    col = st.session_state["col"]
    col_notna = col[col["Fundamental Rating"].notna()]
    df = col_notna
    
    bar = df.sort_values(by = "MC (Billion)", ascending = True)
    
    # Color
    
    color = st.selectbox(label = "Color", options = [None, "Sector", "Subsector"])
    
    # Hover Data
    
    hover_data = [df.index] + ["Sector", "Subsector", "MC (Billion)", "P", "FV", "FV (%)"]
    
    # Plot Data
    
    customdata, hovertemplate = customdata_hovertemplate.ch(df = df, hover_data = hover_data)
    
    fig = px.bar(data_frame = bar,
                 x = "MC (Billion)",
                 y = bar.index,
                 color = color,
                 hover_data = hover_data,
                 text = "FV (%)",
                 width = 1000,
                 height = 1000)
    
    fig.update_traces(customdata = customdata, hovertemplate = hovertemplate, textposition = "outside")
    
    st.plotly_chart(figure_or_data = fig, use_container_width = True)