import streamlit as st
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
st.title("welcome to my project ")
data=pd.read_csv(r"C:\Users\mdfir\Downloads\placement.csv")
print(data)

x=data[["cgpa"]]
y=data["package"]
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=.2,random_state=42)
model=LinearRegression()
print(x_train)
model.fit(x_train,y_train)
pred=model.predict(x_test)
print(pred)
score=r2_score(y_test,pred)
print(score)