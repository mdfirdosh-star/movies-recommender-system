import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn .model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn .compose import ColumnTransformer
from sklearn .preprocessing import LabelEncoder,StandardScaler,OneHotEncoder,OrdinalEncoder,FunctionTransformer,MinMaxScaler
from sklearn .pipeline import Pipeline
import pickle 

st.title("📈 Welcome to my LogesticRegression model prediction")
st.subheader("LogesticRegression predict the value ")
file=st.file_uploader("uplode the file:",type=["csv"])
st.write("uplode the file ")
if file is not None :
    data=pd.read_csv(file)
    st.success("file is uploded")
    st.dataframe(data.head())
    # use pickle file 
    p=pickle.load(open("logesticlr.pkl","rb"))


    total_bill=st.sidebar.number_input("1.enter your value of  total bill")
    tip=st.sidebar.number_input("2.enter your value of tip ")
    sex=st.sidebar.text_input("3.choise the options('male','female')")
    day=st.sidebar.text_input('4.choise the options("Sat","Sun","Thur","Fri")')
    time=st.sidebar.text_input("5.choise the options('Dinner','Lunch')")
    size=st.sidebar.number_input("6.enter your value of  size")
    input_vau=pd.DataFrame({"total_bill":[total_bill],"tip":[tip],"sex":[sex],"day":[day],"time":[time],"size":[size]})
    st.dataframe(input_vau)
    Y_pred=p.predict(input_vau)
    st.write(f"pridict the value smoker and notsmoker:{Y_pred}")
    if Y_pred==0:
         st.success("the pridict value is Notsmoker")
    else:
          st.success("the pridict value is smoker")