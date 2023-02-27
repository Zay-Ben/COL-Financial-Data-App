import streamlit as st
from datetime import date
import pandas as pd
import plotly.express as px
import numpy as np
import customdata_hovertemplate
st.title(body = "Fundamental and Technical")
st.caption(body = date.today())
st.markdown(body = "* Bubble Size - MC (Million)")
st.markdown(body = "* Horizontal Axis - P/FV")
st.markdown(body = "* Vertical Axis - P/52H")
if "col" in st.session_state:
    
    # Import Data
    
    col = st.session_state["col"]
    col_notna = col[col["Fundamental Rating"].notna()]
    df = col_notna
    
    # Color
    
    color = st.selectbox(label = "Color", options = [None, "Sector", "Subsector"])
    
    # Options
    
    col1, col2 = st.columns(2)
    
    with col1:
        advance = st.checkbox(label = "Advance")
        if advance:
            hover_data = [df.index] + ["Sector", "Subsector", "MC (Billion)", "P", "FV", "FV (%)", "P/FV", "52H", "52H (%)", "P/52H"]
            color = "Trend"
            facet_row = "Technical Rating"
            facet_col = "Fundamental Rating"
            height = 1500
        else:
            hover_data = [df.index] + ["Sector", "Subsector", "MC (Billion)", "P", "FV", "FV (%)", "P/FV", "52H", "52H (%)", "P/52H", "Trend", "Technical Rating", "Fundamental Rating"]
            color = color
            facet_row = None
            facet_col = None
            height = 500
            
    with col2:
        ticker = st.checkbox(label = "Ticker")
        if ticker:
            text = df.index
        else:
            text = None
            
    # Plot Data
    
    customdata, hovertemplate = customdata_hovertemplate.ch(df = df, hover_data = hover_data)
    
    fig = px.scatter(data_frame = df,
                     x = "P/FV",
                     y = "P/52H",
                     color = color,
                     size = "MC (Billion)",
                     hover_data = hover_data,
                     text = text,
                     facet_row = facet_row,
                     facet_col = facet_col,
                     width = 1000,
                     height = height)
    
    fig.update_traces(customdata = customdata, hovertemplate = hovertemplate)
    
    st.plotly_chart(figure_or_data = fig, use_container_width = True)
