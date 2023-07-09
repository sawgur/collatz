import streamlit as st
import numpy as np
import pandas as pd
from time import sleep

st.title("Some patterns you may notice:")
st.title("")
st.title("The 9-8 Cycle:")
st.write("""
When we start with the number 500, we see large spikes in value. This is the 9-8 Cycle.

A number with an odd digit in the tens place and a 9 in the ones place, when multiplied by 3 and added to 1, results in a new number with 8 in the ones place.
If the new number has an ODD tens place, we get the 9-8 cycle. When the new number is divided by 2, we get a number with 9 in the ones place. 
If this number has an ODD tens place, the cycle continues. The cycles keeps continuing until we get a number with an EVEN tens place and an 8 in the ones.

With the initial value of 500, this pattern starts at the 55th iteration and ends at the 66th.

5 out of every 100 numbers will result in this cycle, meaning that for any given initial number, there is a 20% chance of the 9-8 cycle happening!
""")
st.title("")
st.title("Break to 2:")
st.write("""
After every 9-8 Cycle, The Collatz Conjecture will Break to 2 (Bt2). 

Once the 9-8 Cycle ends, the values that we get as we run through the operations will ALWAYS end up with peaks of 4 or 2 in the ones place of the value.

Coupled with this, the lows will always be odd numbers other than 9, and if the low is even, we will end the process soon.
""")
st.title("")
st.title("Powers of 2:")
st.write("""
Working backwards, we know that a power of two will immediately go to 1 once ran through the operations. 
This is because any power of 2 has only been multiplied by 2, and can therefore be divided by 2 endlessly until it is equal to (2, two!! Haha!) 1.

From this logic, we know that any time we get to a power of 2, the process will terminate. 
Starting with 16, every OTHER power of 2 is reachable via multiplying a number by 3 and adding 1. Of course, the probability of reaching such a number becomes exponentially harder and harder.

To get the number 256, we need to get to the number 85. I ran a program to find a number that could end up becoming 85 after under going The Collatz Conjecture.

...

From numbers 1-281676747 (yes really) not a SINGLE number EVER becomes 85, so we could never end up with 256. For all of the following powers of 2, we would need an exponentially higher number.

Interesting, no?
""")



