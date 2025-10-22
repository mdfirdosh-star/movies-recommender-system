import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
st.title("welcome to my project")
file=st.file_uploader("uplode file",type=["csv"])
if file:
    data=pd.read_csv(file)
    st.dataframe(data.head())

# Sample data
x = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
y = np.array([2, 4, 5, 4, 5])

# Model training
model = LinearRegression()
model.fit(x, y)

# Prediction
y_pred = model.predict(x)

# Plot
plt.scatter(x, y)
plt.plot(x, y_pred, color='red')
plt.show()