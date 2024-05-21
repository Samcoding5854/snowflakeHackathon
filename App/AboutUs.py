import streamlit as st

def ABOUTUS():
    st.title('About Us')
    st.write("""
    Welcome to our Streamlit app! We are a team of developers passionate about creating 
    innovative solutions using Streamlit.
    """)
    
    st.subheader('Team Members')
    st.write("""
    Meet the minds behind this project:
    """)
    
    # Member 1
    st.write("*Darsh Baxi*")
    st.image('darsh.jpg', width=200)
    st.write("GitHub: [Darsh Baxi](https://github.com/darshbaxi)")
    st.write("LinkedIn: [Darsh Baxi](https://www.linkedin.com/in/darsh-baxi-81350124a/)")
    
    # Member 2
    st.write("*Samarth Sahu*")
    st.image('sam.jpg', width=200)
    st.write("GitHub: [Samarth Sahu](https://github.com/Samcoding5854/)")
    st.write("LinkedIn: [Samarth Sahu](https://www.linkedin.com/in/samarth-sahu/)")

    st.image('logo.png', caption='Our Logo', use_column_width=True)
    st.write("""
    Feel free to explore our app and reach out to us for any questions or feedback!
    """)