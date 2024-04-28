import streamlit as st

# Initialize login status in session state
if 'login_successful' not in st.session_state:
    st.session_state.login_successful = False

# Login Page
def login_page():
    st.title("Welcome to Incoding's Page")

    col1, col2 = st.columns(2)  # Divide the page into two columns

    with col1:
        st.image('https://github.com/nicolasea17/Capstone_Project/blob/main/Incoding%20Picture.png?raw=true', 
                 width=250)  # Set the width of the image

    with col2:
        st.image('https://github.com/nicolasea17/Capstone_Project/blob/main/OSB%20Picture.png?raw=true', 
                 width=250)  # Set the width of the image

    username = st.text_input('Username')
    password = st.text_input('Password', type='password')

    if st.button('Sign In'):
        if username == 'admin' and password == '1234':
            st.session_state.login_successful = True  # Set login status to True
            st.experimental_rerun()  # Rerun the script to hide the login page
        else:
            st.error('Invalid credentials')

# Page after successful login
def prediction_page():
    st.markdown("<h1 style='text-align: center; font-size: 24px;'>Website Development Hourly Rate Prediction</h1>", unsafe_allow_html=True)

    # Create a single column to center the image
    col_image = st.columns([1, 2, 1])  # This creates three columns, and the image will be in the middle one

    with col_image[1]:  # Index 1 is the middle column
        st.image('https://github.com/nicolasea17/Capstone_Project/blob/main/MachineLearning_PriceElasticity.png?raw=true',
                 width=300)  # Display the image centered and smaller

    # Description of the Machine Learning model
    st.write("Please provide information on the customer's posting to predict the hourly rate. This tool uses a machine learning model to analyze historical data and determine the most accurate hourly rates based on similar project descriptions and client budgets.")

def main():
    # Check if logged in
    if st.session_state.login_successful:
        prediction_page()  # Display the prediction page
    else:
        login_page()  # Display the login page

if __name__ == '__main__':
    main()
