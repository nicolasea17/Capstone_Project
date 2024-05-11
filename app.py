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

def preprocess_and_predict(input_data, client_country_gdp):
    try:
        # Calculate log of GDP and predict the cluster
        input_data['GDP'] = np.log(client_country_gdp)
        input_data['GDP_cluster'] = kmeans.predict(input_data[['GDP']])
        
        # Process the input data through the preprocessor pipeline
        processed_data = preprocessor.transform(input_data.drop(['GDP'], axis=1))
        prediction = model.predict(processed_data)
        return prediction
    except Exception as e:
        logging.error(f"Error during preprocessing or prediction: {e}")
        return None

def prediction_page():
    st.title("Customer Tailored Hourly Rate Prediction")
    
    # Manual entries for the sake of completeness
    job_title = st.text_input('Job Title')
    ex_level_demand = st.selectbox('Experience Level Demand', ['Entry Level', 'Intermediate', 'Expert'])
    description = st.text_input('Project Description')
    technical_tool = st.text_input('Technical Tool Used')
    applicants_num = st.selectbox('Number of Applicants', ['Less than 5', '10 to 15', '15 to 20', '20 to 50', '50+'])
    client_country = st.text_input('Client Country')
    spent = st.number_input('Budget Spent', format="%.2f")
    # Assuming GDP data is manually entered or derived from another source
    client_country_gdp = st.number_input('GDP of Client Country', format="%.2f")

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

        prediction = preprocess_and_predict(input_data, client_country_gdp)
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
