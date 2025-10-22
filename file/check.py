import streamlit as st
import pandas as pd
import pickle

st.title("hello")

data=pickle.load(open("./logesticlr.pkl","rb"))

total_bill=st.sidebar.number_input("1.enter your value of  total bill")
tip=st.sidebar.number_input("2.enter your value of tip ")
sex=st.sidebar.text_input("3.choise the options('male','female')")
day=st.sidebar.text_input('4.choise the options("Sat","Sun","Thur","Fri")')
time=st.sidebar.text_input("5.choise the options('Dinner','Lunch')")
size=st.sidebar.number_input("6.enter your value of  size")
input_vau=pd.DataFrame({"total_bill":[total_bill],"tip":[tip],"sex":[sex],"day":[day],"time":[time],"size":[size]})

pred=data.predict(input_vau)

if st.button("predict"):
    st.success(pred)