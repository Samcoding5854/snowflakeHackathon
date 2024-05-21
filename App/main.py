import streamlit as st
import re
import snowflake.connector
from auth import login,authenticated,signup
from detectGame import detect_Game


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
        app = st.sidebar.selectbox('Navigation', ['detectGame'])
        if app == "Chat":
           detect_Game()
    else:
        option = st.selectbox('Choose an option', ['Login', 'Sign Up'])
        if option == 'Sign Up':
            signup(ctx)
        else:
            login(ctx)

          
MAIN()