import streamlit as st
st.write('# Largest Number')
num1= st.number_input('number 1')
num2 = st.number_input('number 2')
num3 = st.number_input('number 3')

if (num1 >= num2) and (num1 >= num3):
   largest = num1
elif (num2 >= num1) and (num2 >= num3):
   largest = num2
else:
   largest = num3

st.write('# Answer is ',largest)
