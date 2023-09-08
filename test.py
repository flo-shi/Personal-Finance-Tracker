import streamlit as st
import numpy as np
import pickle

# Load the saved model parameters
with open("linear_regression_model.pkl", "rb") as f:
    model_parameters = pickle.load(f)

coefficients = model_parameters["coefficients"]
intercept = model_parameters["intercept"]

# --- webpage name ---
st.set_page_config(page_title="Linear Regression", page_icon="", layout="wide")

# --- header section ---
st.header("Personal Finance Tracker")
st.write(
    "Hello my name is Florence, I'm 23 and this will be my first data science project."
)
st.write(
    "We will predict my personal finance expenses based on my expenditure for the past few months. The model makes use of linear regression."
)

st.write("---")
column_1, column_2 = st.columns((1, 2))
with st.container():
    with column_1:
        st.write("##")
        st.subheader("Plot of expenditure over the last few months.")
