import streamlit as st
import pickle 
import pandas as pd
import pickle
import os

current_dir = os.path.dirname(__file__)
model_path = os.path.join(current_dir, "model (1).pkl")

with open(model_path, "rb") as f:
    model = pickle.load(f)


st.title("welcome to my LogesticRegression")



Age=st.sidebar.number_input("enter the age ")
Fare=st.sidebar.number_input("enter the Fare")
Family=st.sidebar.number_input("enter the Family")
input_val=pd.DataFrame({"Age":[Age],"Fare":[Fare],"Family":[Family]})
st.dataframe(input_val)
pred= model.predict(input_val)
st.write("my predict value:",pred)
st.success("my prediction is successfuly is done ")
if pred ==1 :
    st.write("the people is servived")
else:
    st.write("the people is Died")
