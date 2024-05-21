import streamlit as st
import re



def creds(ctx):
    user = st.session_state.get('user', '').strip()
    passwd = st.session_state.get('passwd', '').strip()
    
    if not passwd:
        st.warning('Password cannot be empty')
        st.session_state['authenticated'] = False
    else:
        sql = f"""
        SELECT * FROM USERS
        WHERE USERNAME = '{user}' AND PASSWORD = '{passwd}'
        """
        data = ctx.cursor().execute(sql).fetchone()
        if data==None:
            st.error('Invalid credentials')
            st.session_state['authenticated'] = False    
        elif len(data) > 0:
            st.session_state['authenticated'] = True
            st.rerun()
        else:
            st.error('Invalid credentials')
            st.session_state['authenticated'] = False
            
def validate_password(password):
    # Regex pattern to enforce password criteria
    pattern = r"^(?=.[A-Z])(?=.\d)[A-Za-z\d]{8,}$"
    if re.match(pattern, password):
        return True
    else:
        return False
    
    
def signup(ctx):
    st.title('Sign Up')
    user = st.text_input('Username', key='signup_user').strip()
    email = st.text_input('Email', key='signup_email').strip()
    passwd = st.text_input('Password', type='password', key='signup_passwd').strip()
    
    if st.button('Sign Up'):
        if user and email and passwd:
            # Check if the username already exists
            if not validate_password(passwd):
                st.error("Password must have at least one capital letter, one number, no special characters, and a minimum length of eight characters.")
            else:
                check_user_sql = f"""
                SELECT * FROM USERS
                WHERE USERNAME = '{user}'
                """
                existing_user = ctx.cursor().execute(check_user_sql).fetchall()
                if existing_user:
                    st.error('Username already exists. Please log in.')
                else:
                    insert_sql = f"""
                    INSERT INTO USERS (USERNAME, PASSWORD, EMAIL)
                    VALUES ('{user}', '{passwd}', '{email}')
                    """
                    try:
                        ctx.cursor().execute(insert_sql)
                        st.success('Account created successfully! Please log in.')
                        st.session_state['signup_complete'] = True
                        st.rerun() 
                    except Exception as e:
                        st.error(f"Error creating account: {e}")
        else:
            st.error('All fields are required.')

def login(ctx):
    st.title('Login')
    st.text_input(label="Username: ", key="user")
    st.text_input(label="Password: ", type="password", key="passwd")
    if st.button('Log In'):
        creds(ctx)

def authenticated():
    return st.session_state.get('authenticated', False)