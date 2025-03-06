import streamlit as st
from streamlit.user_info import UserInfoProxy
import re
import streamlit_authenticator as stauth
from google.cloud import firestore


from firebase_tools import get_user_db, get_firestore_collection
from form_templates import experience_form

import datetime
from typing import Optional

### --- UI --- ###

def sidebar_account():
    st.sidebar.divider()
    sidebar_col1, sidebar_col2 = st.sidebar.columns(2)
    if st.experimental_user.is_logged_in:
        get_user_db()
        with sidebar_col1:
            if st.button("Logout", type="tertiary", key="logout_button"):
                st.logout()
                st.switch_page("content/1_homepage.py")

        with sidebar_col2:
            if st.button(f"Your Account: {st.experimental_user.email}", type='primary', key="your_account_button"):
                st.switch_page("content/4_your_content.py")
            
    else:
        with sidebar_col1:
            if st.button("Login", type="primary", key="login_button"):
                login_user()
                get_user_db()

def create_experience_ui(id: int, existing_experience: bool, title: Optional[str]=""):
    with st.expander(f"Experience #{f"{id:02}"} {title}"):
        experience_form(id, existing_experience)

### --- Global Functions --- ###

def login_user():
    st.login()

def get_number_of_existing_experiences() -> int:
    collection = get_firestore_collection("current_experience")
    no_of_documents = collection.count().get()[0][0].value

    return int(no_of_documents)

def generate_current_experience():
    """
    Generate and display current experience entries from a Firestore collection.

    This function retrieves documents from the "current_experience" Firestore collection
    and creates an experience entry for each document using the `create_experience_ui` function.
    Each entry is displayed with its role and organization. If there are no documents in
    the collection, the function returns None.

    Returns:
        str: None if no documents are found, otherwise the function does not return a value.
    """
    experience_collection = get_firestore_collection("current_experience")
    no_of_documents = experience_collection.count().get()[0][0].value
    if not any(experience_collection.stream()):
        return None
    
    for doc in experience_collection.stream():

        doc_dict = doc.to_dict()
        role = doc_dict.get("role", "")
        organization = doc_dict.get("organization", "")
        at_string = "@" if organization else ""
        title = f"{role} {at_string} {organization}"
        id_int = int(doc.id.split("_")[-1])


        # Call create_experience with the appropriate number
        create_experience_ui(id=id_int, existing_experience=True, title=title)

    