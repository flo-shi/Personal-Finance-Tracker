import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pickle

# Load the saved model parameters
with open("linear_regression_model.pkl", "rb") as f:
    model_parameters = pickle.load(f)

coefficients = model_parameters["coefficients"]
intercept = model_parameters["intercept"]
x = model_parameters["x"]
y = model_parameters["y"]
pred_y = model_parameters["pred_y"]

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

# ------- first section, making a plot ------
column_1, column_2 = st.columns((1, 2))
with st.container():
    with column_1:
        st.write("##")
        st.write("##")
        st.write("##")
        st.write("##")
        st.write("##")
        st.write("##")
        st.subheader("Plot of expenditure over the first few months of the year.")
    with column_2:

        def plot():
            (
                fig,
                ax,
            ) = (
                plt.subplots()
            )  # working with matpotlib in a way that is compatible with sreamlit
            ax.plot(x, y)
            ax.set_title("Month against expenditure")
            ax.set_ylabel("Expenditure")
            ax.set_xlabel("Months")
            return fig

        fig = plot()
        st.pyplot(fig)

# ---- second section ----- plot of linear regression
st.write("---")
column_3, column_4 = st.columns((1, 2))
with st.container():
    with column_3:
        st.write("##")
        st.write("##")
        st.write("##")
        st.write("##")
        st.write("##")
        st.write("##")
        st.subheader("Plot of linear regression of the libe graph above.")
    with column_4:

        def linReg():
            fig, ax = plt.subplots()
            ax.plot(x, pred_y)
            ax.set_title("Month against predicted expenditure")
            ax.set_xlabel("Months")
            ax.set_ylabel("Predicted expenditure")
            return fig

        fig = linReg()
        st.pyplot(fig)

# ---- third section ------ collecting user inputs
st.write("---")
with st.container():
    st.write("##")
    st.subheader(
        "Estimation of predicted expenditure for the remaining months of the year"
    )
    st.write(
        "Using the above model we will predict the expenditure for the remaining months of the year by collecting user input"
    )

user_input, pred = st.columns(2)
# collecting user input
with user_input:
    months = st.number_input("Enter a number of any month", min_value=1, max_value=12)

# perform manual prediction
with st.container():

    def man_pred(months):
        return coefficients * months + intercept

    estimate = int(man_pred(months))

# display results
with pred:
    st.write("The estimated monthly expenditure for this month is:")
    st.write(estimate)
