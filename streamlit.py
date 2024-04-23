import streamlit as st

def main():
    st.title("Welcome to Incoding's Page")

    # Display the first image with a fade-in animation
    st.image('https://github.com/nicolasea17/Capstone_Project/blob/main/Incoding%20Picture.png?raw=true', 
             width=250,
             output_format='PNG', # Ensure that the output format is PNG to support CSS styling
             caption="Incoding Picture",
             use_column_width='always',
             style='border: 2px solid #cccccc; border-radius: 10px; padding: 10px; animation: fadeIn 2s;')

    # Add spacing
    st.write("")

    # Display the second image with a fade-in animation
    st.image('https://github.com/nicolasea17/Capstone_Project/blob/main/OSB%20Picture.png?raw=true', 
             width=250,
             output_format='PNG', # Ensure that the output format is PNG to support CSS styling
             caption="OSB Picture",
             use_column_width='always',
             style='border: 2px solid #cccccc; border-radius: 10px; padding: 10px; animation: fadeIn 2s;')

    # Align images in the middle
    st.markdown("""
    <style>
    .stImage > img {
        display: block;
        margin-left: auto;
        margin-right: auto;
        opacity: 0; /* Hide images by default */
    }
    @keyframes fadeIn {
        from { opacity: 0; }
        to   { opacity: 1; }
    }
    </style>
    """, unsafe_allow_html=True)

    # Trigger animation with JavaScript
    st.markdown("""
    <script>
    setTimeout(function(){
        document.querySelectorAll(".stImage > img").forEach(function(img){
            img.style.opacity = "1";
        });
    }, 100);
    </script>
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
