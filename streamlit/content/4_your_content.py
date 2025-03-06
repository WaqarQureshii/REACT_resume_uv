import streamlit as st

from dependencies import login_user, generate_current_experience, get_number_of_existing_experiences, find_next_experience_id
from form_templates import contact_form, experience_form
from firebase_tools import create_firestore_document, get_user_db, upload_firebase_db


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
            db = get_user_db()

            id = find_next_experience_id()

            document_title = f"experience_{id:02}"          

            create_firestore_document(db,"current experience", document_title)
            upload_firebase_db("existing_experience",
                               document_title,
                               organization = "",
                               present =False,
                               role = "",
                               start_date = "",
                               end_date = "",
                               location="")
            experience_form(id, existing_experience=False)

