import streamlit as st

st.title("power caluclator")
st.write("enter a number")

n= st.number_input("number", value=1,step=1)

sq=n**2
cube=n**3
fithpw=n**5


st.write("square of n is",sq)
st.write("cube is ",cube)
st.write("fithpower is",fithpw)
