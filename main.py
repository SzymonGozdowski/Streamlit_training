import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Interactive Math Graphs")

# Selectbox for graph choice
option = st.selectbox(
    "Choose a function to plot:",
    ["sin(x)", "cos(x)", "tan(x)", "exp(x)", "log(x)"]
)

# Generate x values
x = np.linspace(-10, 10, 400)

# Compute y based on user choice
if option == "sin(x)":
    y = np.sin(x)
elif option == "cos(x)":
    y = np.cos(x)
elif option == "tan(x)":
    # mask values where tan explodes
    y = np.tan(x)
    y[np.abs(y) > 10] = np.nan
elif option == "exp(x)":
    y = np.exp(x)
elif option == "log(x)":
    x = np.linspace(0.1, 10, 400)  # avoid log(0)
    y = np.log(x)

# Plot
fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_title(f"Graph of {option}")
ax.grid(True)

st.pyplot(fig)
