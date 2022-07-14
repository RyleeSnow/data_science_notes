import streamlit as st
import pandas as pd
import numpy as np
import time
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.figure_factory as ff
import altair as alt
from PIL import Image
import base64

# Markdown
st.title("This is a Markdown title")
st.header("This is a Markdown header")
st.subheader("This is a Markdown subheader")

st.markdown("# This is a Markdown L1 title")
st.markdown("## This is a Markdown L2 title")
st.markdown("### This is a Markdown L3 title")

st.markdown("Normal markdown texts")
st.markdown("***Markdown texts in bold and italic***")
st.text("Special texts.")

st.markdown("""
This is a Markdown list：
- 1989 
- reputation
- lover
""")

st.text("You can also write a formula:")
st.latex("\sum_{i=1}^{n}")

# Matplotlib
arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)
plt.title("matplotlib plot")
st.pyplot(fig)

# Interactive
number = st.number_input("Insert a number", 123)
st.write("Your input：", number)

# st.write ()
# write(data_frame) : Displays the DataFrame as a table.
# write(func) : Displays information about a function.
# write(module) : Displays information about the module.
# write(dict) : Displays dict in an interactive widget.
# write(obj) : The default is to print str(obj).
# write(mpl_fig) : Displays a Matplotlib figure.
# write(altair) : Displays an Altair chart.
# write(keras) : Displays a Keras model.
# write(graphviz) : Displays a Graphviz graph.
# write(plotly_fig) : Displays a Plotly figure.
# write(bokeh_fig) : Displays a Bokeh figure.
# write(sympy_expr) : Prints SymPy expression using LaTeX.
# write(markdown):

# Numbers and Texts
st.write(1234)
st.write("1234")
st.write("1 + 1 = ", 2)

# Dict
st.write({"a": [1, 2, 3],
          "b": [2, 3, 4]})

# Pandas数据框
df_1 = pd.DataFrame({
    "a": [1, 2, 3, 4, 5],
    "b": [4, 5, 6, 7, 8]})

st.write(df_1)
st.dataframe(df_1)

# Markdown
st.write("Hello, *World!* :sunglasses:")

# Draw
df_2 = pd.DataFrame(
    np.random.randn(200, 3),
    columns=["a", "b", "c"]
)

c = alt.Chart(df_2).mark_circle().encode(
    x="a", y="b", size="c", color="c", tooltip=["a", "b", "c"])
st.write(c)
