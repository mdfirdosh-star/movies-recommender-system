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
    x=data[["total_bill","tip","sex","day","time","size"]]
    y=data["smoker"].values

    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
    l=LabelEncoder()

    y_train_t=l.fit_transform(y_train)
    y_test_t=l.transform(y_test)

    step_1=ColumnTransformer([("onehotencoder",OneHotEncoder(handle_unknown="ignore"),[2,3,4])],remainder="passthrough")
    step_2=ColumnTransformer([
("MinMaxScaler",MinMaxScaler(),slice(0,14))
],remainder="passthrough")
    step_3=ColumnTransformer([
    ("FunctionTransformer",FunctionTransformer(np.log1p),slice(0,14))
],remainder="passthrough")
    step_4=LogisticRegression()
    pip=Pipeline([
    ("step_1",step_1),
    ("step_2",step_2),
    ("step_3",step_3),
    ("step_4",step_4),

    #  create the piuckle file 
])# model train 
    pip.fit(x_train,y_train_t)
    st.success("model train success")

    total_bill=st.sidebar.number_input("1.enter your value of  total bill",min_value=1,max_value=20)
    tip=st.sidebar.number_input("2.enter amount your tip ",min_value=1,max_value=3)
    sex = st.sidebar.radio("3. Choose your sex:", ('male', 'female'))
    day = st.sidebar.selectbox("4. Choose the day:", ("Thur", "Fri", "Sat", "Sun"))
    time = st.sidebar.radio("5. Choose time of meal:", ('Lunch', 'Dinner'))
    size=st.sidebar.number_input("Enter size of group")
    input_vau=pd.DataFrame({"total_bill":[total_bill],"tip":[tip],"sex":[sex],"day":[day],"time":[time],"size":[size]})
    st.dataframe(input_vau)
    Y_pred=pip.predict(input_vau)
    st.write(f"pridict the value smoker and notsmoker:{Y_pred}")
    if Y_pred==0:
         st.success("the pridict value is Notsmoker")
    else:
          st.success("the pridict value is smoker")