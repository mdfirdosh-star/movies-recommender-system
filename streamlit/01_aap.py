import streamlit as st
# adding titile of your aap
st.title("hello programer")
st.subheader("welcome to my chnnel")
st.write("chose a programming languge ")
st.text("welcome to first streamit.app")
var=st.selectbox("my fav team in ipl:",["kkr","mi","cks","rcb"])
st.write(f"my fev team is {var}")
st.success(f"you choise the team {var}")
