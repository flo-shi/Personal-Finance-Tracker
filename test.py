import streamlit as st
import numpy as np
import pickle

# Load the saved model parameters
with open("linear_regression_model.pkl", "rb") as f:
    model_parameters = pickle.load(f)

coefficients = model_parameters["coefficients"]
intercept = model_parameters["intercept"]

# --- webpage name ---
st.set_page_config(page_title="Linear Regression", page_icon="", layout="centered")

# --- header section ---
st.header("Personal Finance Tracker")
