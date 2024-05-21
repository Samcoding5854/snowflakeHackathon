import streamlit as st
import re
import snowflake.connector
from auth import login,authenticated,signup
from detectGame import DETECT_GAME
from AboutUs import ABOUTUS

st.set_page_config(
        page_title="Clued In: AI Detective",
        page_icon="🕵‍♂",
        layout="wide",  # 'centered' or 'wide'
        initial_sidebar_state="expanded"  # 'auto', 'expanded', 'collapsed'
    )

def CONNECTION():
    ctx = snowflake.connector.connect(
        user="DCB",
        password="Darsh@12345",
        account="vzbhpmy-fo16400",
        database="USER_AUTH_DB",
        schema="PUBLIC"
    )
    return ctx



def MAIN():
    ctx=CONNECTION()  
    if st.session_state.get('signup_complete'):
        st.session_state['signup_complete'] = False  # Reset the flag
        login(ctx)
    elif authenticated():
        st.sidebar.title('Detective Game')
        app = st.sidebar.selectbox('', ['Detect Game','About Us'])
        if app == "Detect Game":
           DETECT_GAME()
        else:
            ABOUTUS()
    else:
        option = st.selectbox('Choose an option', ['Login', 'Sign Up'])
        if option == 'Sign Up':
            signup(ctx)
        else:
            login(ctx)

          
MAIN()