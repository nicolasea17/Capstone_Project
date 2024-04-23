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
            st.success('Logged in as {}'.format(username))
            st.session_state.login_successful = True  # Set login status to True
            st.experimental_rerun()  # Rerun the script to hide the login page
        else:
            st.error('Invalid credentials')

# Page after successful login
def prediction_page():
    st.title("Website Development Hourly Rate Prediction")

    # Display the image centered
    st.image('https://github.com/nicolasea17/Capstone_Project/blob/main/MachineLearning_PriceElasticity.png?raw=true',
             use_column_width=True)

def main():
    login_page()  # Display the login page

    # If the script is rerun due to successful login, display the prediction page
    if st.session_state.login_successful:
        prediction_page()  # Display the prediction page

if __name__ == '__main__':
    main()
