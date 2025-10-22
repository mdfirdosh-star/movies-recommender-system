import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

st.title("📈 Simple Linear Regression App")

st.write("This app lets you perform simple linear regression on your data.")

# Upload CSV file
uploaded_file = st.file_uploader("Upload a CSV file (with two columns: X and Y)", type=["csv"])

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.write("### Data Preview:")
    st.write(data.head())

    if not data.empty:
        x = data[["cgpa"]]
        y= data["package"]
        x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=.2,random_state=42)
        model = LinearRegression()
        model.fit(x_train,y_train)
        input_val =st.number_input("enter your value")
        Y_pred = model.predict([[input_val]])
      

        st.success("✅ Model trained successfully!")

        st.write("pricict value", Y_pred)
    else:
        st.error("Please upload a CSV file with exactly two columns (X and Y).")
else:
    st.info("Please upload a CSV file to start.")
