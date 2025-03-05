import streamlit as st
from dependencies import login_user, generate_current_experience
from form_templates import contact_form
from google.cloud import firestore

from form_templates import add_experience_form
from dependencies import get_number_of_existing_experiences


if not st.experimental_user.is_logged_in:
    login_user()
    
else:
    st.header(f"Welcome, {st.experimental_user.name}!")
    col1, col2 = st.columns([1,10])

    col1.text("Your Resume Content")

    contact_tab, current_experience_tab, add_experience_tab, education_tab, certification_tab = col2.tabs(["Contact", "Edit Current Experience", "Add New Experience", "Education", "Certification"])

    with contact_tab:
        contact_form()


    #TODO dynamic expander name
    with current_experience_tab:
        
        generate_current_experience()
        
    with add_experience_tab:
        if st.button("Add Experience", "add_experience_button"):
            add_experience_form()
            current_experience_number = get_number_of_existing_experiences()