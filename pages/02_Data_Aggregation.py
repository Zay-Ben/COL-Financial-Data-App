import streamlit as st
import col_financial
import data_preprocessing
import pandas as pd
from datetime import datetime
import numpy as np
import io

st.title(body = "Data Aggregation")

path_col = st.file_uploader(label = "Upload the Microsoft Excel file (xlsx) that contains COL Financial's All Shares Index, Investment Guide, and Technical Guide here.", type = "xlsx")

if st.button("Sample Data"):
    path_col = "inputs/COL.xlsx"
else:
    pass

if path_col:
    
    col_temporary = col_financial.cf(path_col = path_col)
    
    col = data_preprocessing.dp(col_temporary = col_temporary)
    
    buffer = io.BytesIO()
    
    with pd.ExcelWriter(path = buffer, engine = "xlsxwriter") as writer:
        col.to_excel(writer)
        
    writer.save()
        
    st.markdown(body = "Download Data")
    
    st.download_button(label = "data.xlsx", data = buffer, file_name = "data.xlsx")
    
    st.markdown(body = "View Data")
    
    st.dataframe(data = col)
    
    st.session_state["col"] = col
