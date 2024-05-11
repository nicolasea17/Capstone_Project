import streamlit as st
import pandas as pd
import numpy as np
import joblib
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

# Function to load models
@st.cache_resource
def load_models():
    logging.info("Loading models...")
    try:
        model = joblib.load('random_forest_model.joblib')
        kmeans = joblib.load('kmeans_model.joblib')
        preprocessor = joblib.load('preprocessor.joblib')
        logging.info("All models loaded successfully.")
        return model, kmeans, preprocessor
    except Exception as e:
        logging.error(f"Error loading models: {e}")
        return None, None, None

model, kmeans, preprocessor = load_models()

def preprocess_and_predict(input_data):
    try:
        # Process the input data through the preprocessor pipeline
        processed_data = preprocessor.transform(input_data)
        prediction = model.predict(processed_data)
        return prediction
    except Exception as e:
        logging.error(f"Error during preprocessing or prediction: {e}")
        return None

def prediction_page():
    st.title("Customer Tailored Hourly Rate Prediction")
    
    # Dropdown options
    job_title_options = ['Software Developer', 'Data Scientist', 'Project Manager']
    description_options = ['Energy and Utilities', 'Automotive', 'Small Business']
    technical_tool_options = ['Python', 'Excel', 'Tableau']
    applicants_num_options = ['Less than 5', '10 to 15', '15 to 20', '20 to 50', '50+']
    client_country_options = ['USA', 'Canada', 'UK', 'Germany', 'France']

    job_title = st.selectbox('Job Title', job_title_options)
    ex_level_demand = st.selectbox('Experience Level Demand', ['Entry Level', 'Intermediate', 'Expert'])
    description = st.selectbox('Project Description', description_options)
    technical_tool = st.selectbox('Technical Tool Used', technical_tool_options)
    applicants_num = st.selectbox('Number of Applicants', applicants_num_options)
    client_country = st.selectbox('Client Country', client_country_options)
    spent = st.number_input('Budget Spent', format="%.2f")

    if st.button('Predict Hourly Rate'):
        input_data = pd.DataFrame({
            'Job Title': [job_title],
            'EX_level_demand': [ex_level_demand],
            'Description': [description],
            'Technical_Tool': [technical_tool],
            'Applicants_Num': [applicants_num],
            'Client_Country': [client_country],
            'Spent($)': [spent]
        })

        prediction = preprocess_and_predict(input_data)
        if prediction is not None:
            st.write(f"The predicted hourly rate is ${prediction[0]:.2f}")
        else:
            st.error("Prediction failed. Please check the logs.")
def login_page():
    st.title("Welcome to Incoding's Page")
    col1, col2 = st.columns(2)

    with col1:
        st.image('https://github.com/nicolasea17/Capstone_Project/blob/main/Incoding%20Picture.png?raw=true', width=250)

    with col2:
        st.image('https://github.com/nicolasea17/Capstone_Project/blob/main/OSB%20Picture.png?raw=true', width=250)

    username = st.text_input('Username')
    password = st.text_input('Password', type='password')

    if st.button('Sign In'):
        if username == 'admin' and password == '1234':
            st.session_state.login_successful = True
            st.experimental_rerun()
        else:
            st.error('Invalid credentials')

def main():
    if 'login_successful' not in st.session_state:
        st.session_state.login_successful = False

    if st.session_state.login_successful:
        prediction_page()
    else:
        login_page()

if __name__ == '__main__':
    main()
