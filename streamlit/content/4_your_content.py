import streamlit as st

from dependencies import login_user, generate_current_experience, get_number_of_existing_experiences, find_next_id, generate_education
from form_templates import contact_form, experience_form
from firebase_tools import create_firestore_document, get_user_db, upload_firebase_db


if not st.experimental_user.is_logged_in:
    login_user()
    
else:
    st.header(f"Welcome, {st.experimental_user.name}!")
    col1, col2 = st.columns([1,10])

    col1.text("Your Resume Content")

    contact_tab, current_experience_tab, education_tab = col2.tabs(["Contact", "Professional Experience", "Education"])

    with contact_tab:
        contact_form()

    #TODO dynamic expander name
    with current_experience_tab:
        if st.button("Add Experience", "add_experience_button"):
            id = find_next_id("current_experience")

            document_title = f"experience_{id:02}"          

            create_firestore_document("current_experience", document_title)
            upload_firebase_db("current_experience",
                               document_title,
                               organization = None,
                               role = None
                               )
        generate_current_experience()
        

    with education_tab:
        if st.button("Add Education", key="add_education_button"):
            id = find_next_id("education")

            document_title = f"education_{id:02}"

            create_firestore_document("education", document_title)
            upload_firebase_db("education",
                               document_title,
                               degree = "",
                               institution=""
                               )
        generate_education()

