import streamlit as st
from datetime import date 
st.title("hello chai app")
st.subheader("Brewed with streamlit")
st.write("welcome to the first interative aap")
st.header("use selectbox")
options=st.selectbox("your fav chai:",["masala chai ","lemon chai","adrak chai"])
st.write(f"your choice is good: {options}")
st.success("your chai has been brewed ")


# button
st.header("use button")
if st.button("make chai"):
    st.success("your chai is brewed")
else:
    st.write("click the button above")

#  checkbox
st.header("use checkbook")
var=st.checkbox("aad masala")
if var:
    st.success("aad masala is your chai")
else:
    st.success("no add masala your chai if you add masala click the options ")


# radio # options provied 
st.header("use radio ")
tea_add=st.radio("pick your chai bsae:",["suger","honey","nembu","balcksult"])
if tea_add:
    st.success(f"add {tea_add} your chai")


# use slider 
st.header("use slider")
suger=st.slider("suger level",0,5,2)


# number_input 
st.header("use number_input")
cups=st.number_input("how many cup ",min_value=1,max_value=200)
st.write(f" select how many cup : {cups}")

# text_input
st.header("use text_input")
name=st.text_input("enter your name").upper()
if name :
    st.write(f"welcome, {name} your chai on the way")

# time_input
time=st.time_input("select the time")
st.write(f"you are select the time : {time}")

# date_input
st.header("use date input ")
dob=st.date_input("select the date of birth :")
today=date.today()
age=today.year-dob.year-((today.month,today.day)<(dob.month,dob.day))
st.write(f"your age is : {age}")