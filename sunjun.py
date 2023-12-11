import streamlit as st
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

import numpy as np
# import random as r

c1 = st.radio('선의 색을 선택하시오', ['red', 'green', 'blue', 'orange'])
s1 = st.radio('선의 형태를 선택하시오', ['-', ':', '-.', '--'])

fig, ax = plt.subplots()

x = []
y = []
for i in range(-20, 21, 2):   
    x.append(i)
    y.append(3*i*i - 5*1 + 2)

# plt.plot(x,y, 'rs-', linewidth = 2)

plt.plot(x, y, color=c1, linestyle=s1, marker='h')


st.pyplot(fig)