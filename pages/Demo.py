import streamlit as st
import numpy as np
import pandas as pd
from time import sleep

st.title("The Collatz Conjecture")
num = st.slider('Enter a number', 0, 1000, 500)
st.write("""Adjust the slider and watch how the original number changes throughout the graph, and always goes back to 1! 

The Y-Axis represents the value of the number, and the X-Axis represents the # of iterations of the arithmetic operations.
 
Try to see what number gets the most iterations!""")
oldConjectures = [num]

while num >1:

    sleep(0.05)
    if num %2 ==0:
        num /=2

    else:

        num *=3
        num +=1
    oldConjectures.append(num)

chart = st.line_chart(oldConjectures, height=700, width=1000)


