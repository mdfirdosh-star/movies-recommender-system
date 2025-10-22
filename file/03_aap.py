import streamlit as st
st.title("chai test poll")

# use columns 
col1,col2=st.columns(2)
with col1:
    st.header("masala chai")
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQR9_CEIhzU5H0n94eynAvx9WXvJ-lU_85jjQi3_3B9rmzDI9W6Kn-xlqzjmtdTXYlXiI_xDDx4YBLuwiTCiuPmfrAlY2ClOrMFIr7Ucg",  width=200)
    vote1=st.button("masala chai")
with col2:
    st.header("adrak chai")
    st.image("https://budleaf.com/wp-content/uploads/2023/08/Adrak-masala-chai-scaled.jpeg",width=300)
    vote_2=st.button("adrak chai")
if vote_2:
    st.success("thank you for voting for adrak chai")
elif vote1:
  st.success("thank you for voting for masala chai ")

# use sidebar 
name=st.sidebar.text_input("Enter your name")
tea=st.sidebar.selectbox("chose your chai ",["masala","adrak","kesar"])
st.success(f"welcome {name} and your {tea} chai is getting ready ")


# use expender

with st.expander("show chai making instructions"):
    st.write('''

1.boil water with tea leaves,
2.add milk ,
3.aad suger ,
4.aad           
''')
 