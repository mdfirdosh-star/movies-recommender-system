
import streamlit as st
import pandas as pd
import pickle 
st.title("DecisionTreeClassifier pridiction model")

# uplode the data 
file=st.file_uploader("uplode the file ",type=["csv"])
st.write(" please file upload")
if file is not None :
       data=pd.read_csv(file)
       st.success("file upload")
       st.dataframe(data.head())
       model=pickle.load(open("DecisionTreeClassifier.pkl","rb"))
       st.success("my model is prefect train")


# predict the val
       Pclass=st.sidebar.number_input("1.enter your pclass",min_value=1,max_value=3)
       Sex=st.sidebar.radio("2.chose the options ",("Male","Female"))
       Age=st.sidebar.number_input("3.enter your age")
       SibSp=st.sidebar.number_input("1.enter your sipsp",min_value=0,max_value=8)
       Parch=st.sidebar.number_input("1.enter your parch",min_value=0,max_value=6)
       Fare=st.sidebar.number_input("1.enter your fare")
       Embarked=st.sidebar.radio("2.chose the options Embarked ",("S","C","Q"))
       input_val=pd.DataFrame({"Pclass":[Pclass],"Sex":[Sex],"Age":[Age],"SibSp":[SibSp],"Parch":[Parch],"Fare":[Fare],"Embarked":[Embarked]})
       st.dataframe(input_val)


       pred=model.predict(input_val)
       st.success(f"my pridict the value{pred}")
       if pred ==1:
              st.success("people is Servived")
       else: 
              st.success("people is NotServived")
              
              
       