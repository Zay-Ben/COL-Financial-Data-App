import streamlit as st
import col_financial
import data_preprocessing
import pandas as pd
from datetime import datetime
import numpy as np
import io

st.title(body = "Data Aggregation")

path_col = st.file_uploader(label = "Upload the Microsoft Excel file (xlsx) that contains :blue[COL Financial]'s :orange[All Shares Index], :orange[Investment Guide], and :orange[Technical Guide] here.", type = "xlsx")

if path_col:
    
    col_temporary = col_financial.cf(path_col = path_col)
    
    col = data_preprocessing.dp(col_temporary = col_temporary)
    
    buffer = io.BytesIO()
    
    with pd.ExcelWriter(path = buffer, engine = "xlsxwriter") as writer:
        col.to_excel(writer)
        
    writer.save()
    
    st.markdown(body = "Download Data")
    
    st.download_button(label = "col.xlsx", data = buffer, file_name = "col.xlsx")
    
    st.markdown(body = "View Data")
    
    st.dataframe(data = col)
    
    st.session_state["col"] = col