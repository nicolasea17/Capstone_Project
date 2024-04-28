import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load data
@st.cache
def load_data():
    data = pd.read_csv('combined_dataset1-1300.csv')
    # Additional preprocessing can be placed here
    return data

data = load_data()

import streamlit as st
import joblib
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

# Load model
@st.cache(allow_output_mutation=True)
def load_model():
    # Log that the function is being called
    logging.info("Loading model...")
    try:
        # Assuming the model is saved locally in the same directory as the script
        model = joblib.load('random_forest_model.joblib')
        # Log success message
        logging.info("Model loaded successfully.")
        return model
    except Exception as e:
        # Log error message if model loading fails
        logging.error("Error loading model:", e)
        return None

model = load_model()  # Load model

# Initialize login status in session state
if 'login_successful' not in st.session_state:
    st.session_state.login_successful = False

# Login Page
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
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

# Prediction Page
def prediction_page():
    logging.info("Prediction page called.")

    st.markdown("<h1 style='text-align: center; font-size: 24px;'>Website Development Hourly Rate Prediction</h1>", unsafe_allow_html=True)
    col_image = st.columns([1, 2, 1])

    with col_image[1]:
        st.image('https://github.com/nicolasea17/Capstone_Project/blob/main/MachineLearning_PriceElasticity.png?raw=true', width=300)

    st.write("Please provide information on the customer's posting to predict the hourly rate.")

    # User inputs for the prediction
    job_title_options = data['Job Title'].unique().tolist()
    ex_level_demand_options = ['Entry Level', 'Intermediate', 'Expert']
    description_options = [
        'Energy and Utilities', 'Automotive', 'Small Business/Local Business', 'Non-Profit and NGOs',
        'Real Estate', 'Retail (Non-E-commerce)', 'E-Commerce', 'Telecommunications', 'Manufacturing and Industrial',
        'Finance and Banking', 'Media and Entertainment', 'Insurance', 'Healthcare', 'Construction and Engineering',
        'Personal Blogs/Portfolios', 'Hospitality and Travel', 'Government', 'Education', 'Professional Services',
        'Technology and SaaS', 'Technology', 'Retail', 'Finance', 'Entertainment', 'Manufacturing', 'Transportation',
        'Legal', 'Marketing', 'Hospitality'
    ]
    technical_tool_options = data['Technical_Tool'].unique().tolist()
    applicants_num_options = ['Less than 5', '10 to 15', '15 to 20', '20 to 50', '50+']
    client_country_options = data['Client_Country'].unique().tolist()

    job_title = st.selectbox('Job Title', job_title_options)
    ex_level_demand = st.selectbox('Experience Level Demand', ex_level_demand_options)
    description = st.selectbox('Project Description', description_options)
    technical_tool = st.selectbox('Technical Tool Used', technical_tool_options)
    applicants_num = st.selectbox('Number of Applicants', applicants_num_options)
    client_country = st.selectbox('Client Country', client_country_options)
    spent = st.number_input('Budget Spent')

    if st.button('Predict Hourly Rate'):
        logging.info("Predict button clicked.")
        # Preprocessing the input data
        input_data = pd.DataFrame({
            'Job Title': [job_title],
            'EX_level_demand': [ex_level_demand],
            'Description': [description],
            'Technical_Tool': [technical_tool],
            'Applicants_Num': [applicants_num],
            'Client_Country': [client_country],
            'Spent($)': [spent]
        })
        
        logging.info(f"Input data: {input_data}")

        try:
            # Preprocess input data
            preprocessed_data = preprocess_input_data(input_data)
            logging.info(f"Preprocessed data: {preprocessed_data}")

            # Predict using the preprocessed data
            prediction = predict(preprocessed_data)
            logging.info(f"Prediction result: {prediction}")
            st.write(f"The predicted hourly rate is ${prediction[0]:.2f}")
        except Exception as e:
            logging.error(f"Error occurred during prediction: {e}")
            st.error("An error occurred during prediction. Please check the logs for more information.")

def preprocess_input_data(input_data):
    # Preprocessing steps here, if any
    # For now, just return the input data as is
    return input_data

def predict(preprocessed_data):
    # Predict using the loaded model
    prediction = model.predict(preprocessed_data)
    return prediction

# Main function to control page rendering
def main():
    if st.session_state.login_successful:
        prediction_page()
    else:
        login_page()

if __name__ == '__main__':
    main()
