import streamlit as st
from services.persistence.exercise_repository import get_or_create_username

def render_login_wall():
    if st.session_state.get("user_id") is not None:
        return True
    

    st.title("AI Real-Time GYM Coach")
    st.markdown("Enter User_id: ") 
    

    with st.form("login_form", clear_on_submit=False):
        username = st.text_input("Name Unique ID", placeholder="Enter your unique ID")
        submit_button = st.form_submit_button("Start Session", width="stretch")
    
    if submit_button:
        if not username:
            st.error("Please enter a valid User ID.")
            return False
        user = get_or_create_username(username)
        st.session_state["user_id"] = user["id"]
        st.session_state["username"] = user["username"]
        st.rerun()
    return False


