import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image  # Import Image from Pillow

st.write('write here')

if st.checkbox('You can click'):
    st.write('Checkbox was clicked')
    x = np.linspace(-np.pi, np.pi, 400)
    y = np.sin(x)

    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_title("Wykres sin(x)")
    st.pyplot(fig)
