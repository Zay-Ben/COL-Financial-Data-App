import streamlit as st
from datetime import date
import pandas as pd
import plotly.express as px
import numpy as np

st.title(body = "Fundamental and Technical")
st.caption(body = date.today())
st.markdown(body = "* Bubble Size - MC (Million)")
st.markdown(body = "* Horizontal Axis - P/FV")
st.markdown(body = "* Vertical Axis - P/52H")

with st.expander("How to interpret the chart?"):
    st.write(\"\"\"
    The chart above shows some numbers I picked for you.
    I rolled actual dice for these, so they're *guaranteed* to
    be random.
    \"\"\")

if "col" in st.session_state:
    
    # Import Data
    
    col = st.session_state["col"]
    col_notna = col[col["Fundamental Rating"].notna()]
    df = col_notna
    df = df.reset_index()
        
    # Color
    
    color = st.selectbox(label = "Color", options = [None, "Sector", "Subsector"])
    
    # Options
    
    col1, col2, col3 = st.columns(3)
    
    # Advance
    
    with col1:
        advance = st.checkbox(label = "Advance")
        if advance:
            custom_data = ["Ticker"] + ["Sector", "Subsector", "MC (Billion)", "P", "FV", "FV (%)", "P/FV", "52H", "52H (%)", "P/52H", "Trend", "Technical Rating", "Fundamental Rating"]
            color = "Trend"
            facet_row = "Technical Rating"
            facet_col = "Fundamental Rating"
            height = 1500
        else:
            custom_data = ["Ticker"] + ["Sector", "Subsector", "MC (Billion)", "P", "FV", "FV (%)", "P/FV", "52H", "52H (%)", "P/52H"]
            color = color
            facet_row = None
            facet_col = None
            height = 500
            
    # Sweet Spot
    
    with col2:
        sweet_spot = st.checkbox(label = "Sweet Spot")
        
    # Ticker
    
    with col3:
        ticker = st.checkbox(label = "Ticker")
        if ticker:
            text = "Ticker"
        else:
            text = None
            
    # Plot Data
    
    hovertemplate = "<br>".join(["<b>%{customdata[0]}</b>"] + ["<b>" + str(custom_data[i]) + ":</b> %{customdata[" + str(i) + "]}" for i in range(1, len(custom_data))])
    
    fig = px.scatter(data_frame = df,
                     x = "P/FV",
                     y = "P/52H",
                     color = color,
                     size = "MC (Billion)",
                     custom_data = custom_data,
                     text = text,
                     facet_row = facet_row,
                     facet_col = facet_col,
                     width = 1000,
                     height = height)
    
    fig.update_traces(hovertemplate = hovertemplate)
    
    if sweet_spot:
        fig.add_shape(fillcolor = "green",
                      opacity = 0.1,
                      x0 = min(df["P/FV"]),
                      x1 = 1,
                      y0 = 0.9,
                      y1 = max(df["P/52H"]))
    else:
        pass
    
    st.plotly_chart(figure_or_data = fig, use_container_width = True)
