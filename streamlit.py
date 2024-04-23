import streamlit as st

def main():
    st.title("Welcome to Incoding&apos;s Page")

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
            # Redirect to another page or perform actions after login
        else:
            st.error('Invalid credentials')

if __name__ == '__main__':
    main()
