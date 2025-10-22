import streamlit as st
import pickle 
import pandas as pd 
st.title("welcome to my Logestic regression webside ")
st.subheader("pridict the value of 'test preparation course' ")
model=pickle.load(open("./logesticRegression_2.pkl","rb"))
st.write("text",model.feature_names_in_)
st.success("model succussful train ")


st.sidebar.header("fill the all options user")
gender=st.sidebar.radio("chose the options ",["female","mal"])
race_ethnicity=st.sidebar.radio("chose the options ",["group A","group B","group C","group D","group E"])
parental_level_of_education=st.sidebar.radio("chose the options ",["high school","some high school","some college","associate's degree","bachelor's degree","master's degree"])
lunch=st.sidebar.radio("chose the options",["standard","free/reduced"])
math_score=st.sidebar.number_input("enter your math score ")
reading_score=st.sidebar.number_input("enter your reading  score ")
writing_score=st.sidebar.number_input("enter your writing  score ")
user_val=pd.DataFrame({"gender":[gender],"race_ethnicity":[race_ethnicity],"parental_level_of_education":[parental_level_of_education],"lunch":[lunch],"math_score":[math_score],"reading_score":[reading_score],"writing_score":[writing_score]})
st.dataframe(user_val)
pred=model.predict(user_val)
st.success(f"my predicted value is {pred}")




