import streamlit as st

def main():
    st.title('Welcome to Your Application')

    # Create two columns for the images
    col1, col2 = st.beta_columns(2)

    # Display the first image in the first column
    with col1:
        st.image('https://github.com/nicolasea17/Capstone_Project/blob/main/Incoding%20Picture.png?raw=true', use_column_width='always')

    # Display the second image in the second column
    with col2:
        st.image('https://github.com/nicolasea17/Capstone_Project/blob/main/OSB%20Picture.png?raw=true', use_column_width='always')

    username = st.text_input('Username')
    password = st.text_input('Password', type='password')

    if st.button('Sign In'):
        if username == 'your_username' and password == 'your_password':
            st.success('Logged in as {}'.format(username))
            # Redirect to another page or perform actions after login
        else:
            st.error('Invalid credentials')

if __name__ == '__main__':
    main()
