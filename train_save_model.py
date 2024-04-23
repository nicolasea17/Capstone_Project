import streamlit as st
import pandas as pd
import numpy as np
import requests
import joblib
from io import BytesIO

# Function to load the trained Extra Trees model from GitHub
@st.cache(allow_output_mutation=True)
def load_model():
    # URL of the joblib model file on GitHub (Adjust if the path is different)
    model_url = 'https://github.com/nicolasea17/Capstone_Project/blob/main/extra_trees_model.joblib?raw=true'
    response = requests.get(model_url)
    model = joblib.load(BytesIO(response.content))
    return model

model = load_model()  # Load model

# Initialize login status in session state
if 'login_successful' not in st.session_state:
    st.session_state.login_successful = False

# Login Page
def login_page():
    st.title("Welcome to Incoding's Page")
    col1, col2 = st.columns(2)  # Divide the page into two columns

    with col1:
        st.image('https://github.com/nicolasea17/Capstone_Project/blob/main/Incoding%20Picture.png?raw=true', width=250)

    with col2:
        st.image('https://github.com/nicolasea17/Capstone_Project/blob/main/OSB%20Picture.png?raw=true', width=250)

    username = st.text_input('Username')
    password = st.text_input('Password', type='password')

    if st.button('Sign In'):
        if username == 'admin' and password == '1234':
            st.session_state.login_successful = True  # Set login status to True
            st.experimental_rerun()  # Rerun the script to hide the login page
        else:
            st.error('Invalid credentials')

# Prediction Page
def prediction_page():
    st.markdown("<h1 style='text-align: center; font-size: 24px;'>Website Development Hourly Rate Prediction</h1>", unsafe_allow_html=True)
    col_image = st.columns([1, 2, 1])  # This creates three columns, and the image will be in the middle one

    with col_image[1]:  # Index 1 is the middle column
        st.image('https://github.com/nicolasea17/Capstone_Project/blob/main/MachineLearning_PriceElasticity.png?raw=true', width=300)

    st.write("Please provide information on the customer's posting to predict the hourly rate. This tool uses a machine learning model to analyze historical data and determine the most accurate hourly rates based on similar project descriptions and client budgets.")

    # User inputs for the prediction
    job_title = st.selectbox('Job Title', ['Job Title 1', 'Job Title 2'])  # Add actual options
    ex_level_demand = st.selectbox('Experience Level Demand', ['Entry', 'Intermediate', 'Expert'])  # Add actual options
    description = st.text_input('Project Description')
    technical_tool = st.selectbox('Technical Tool Used', ['Tool 1', 'Tool 2'])  # Add actual options
    applicants_num = st.selectbox('Number of Applicants', ['Less than 5', '5-10', 'More than 10'])  # Add actual options
    client_country = st.selectbox('Client Country', ['Country 1', 'Country 2'])  # Add actual options
    spent = st.number_input('Budget Spent')

    if st.button('Predict Hourly Rate'):
        # Assuming the preprocessing and feature preparation are the same as used during model training
        input_data = pd.DataFrame({
            'Job Title': [job_title],
            'EX_level_demand': [ex_level_demand],
            'Description': [description],
            'Technical_Tool': [technical_tool],
            'Applicants_Num': [applicants_num],
            'Client_Country': [client_country],
            'Spent($)': [spent]
        })

        # Predict using the loaded model
        prediction = model.predict(input_data)
        st.write(f"The predicted hourly rate is ${prediction[0]:.2f}")

# Main function to control page rendering
def main():
    if st.session_state.login_successful:
        prediction_page()
    else:
        login_page()

if __name__ == '__main__':
    main()
