
import streamlit as st
import pandas as pd
st.title("data dasbord")
file=st.file_uploader("uplode the file",type=["csv"])
if file:
    data=pd.read_csv(file)
    st.subheader("Data preview")
    st.dataframe(data.head())
if file:
    att=data["attention"].unique()
    sel_att=st.selectbox("selected attention:",att)
    sel_att_1=data[data["attention"]== sel_att]
    st.dataframe(sel_att_1)
    
