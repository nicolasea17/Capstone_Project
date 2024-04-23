import streamlit as st

def main():
    st.title("Welcome to Incoding's Page")

    # Display the first image
    st.image('https://github.com/nicolasea17/Capstone_Project/blob/main/Incoding%20Picture.png?raw=true', width=250)

    # Add spacing
    st.write("")

    # Display the second image
    st.image('https://github.com/nicolasea17/Capstone_Project/blob/main/OSB%20Picture.png?raw=true', width=250)

    # Align images in the middle
    st.markdown("""
    <style>
    .stImage > img {
        display: block;
        margin-left: auto;
        margin-right: auto;
    }
    </style>
    """, unsafe_allow_html=True)

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
