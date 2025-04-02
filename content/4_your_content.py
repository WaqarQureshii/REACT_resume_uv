import streamlit as st

from tools_general import login_user, generate_experience, find_next_id, generate_education, generate_summary
from form_templates import contact_form
from tools_firebase import create_firestore_document, upload_firebase_db, get_firestore_value


if not st.experimental_user.is_logged_in:
    login_user()

elif not get_firestore_value("subscription_status", "subscription_status").get("premium"):
    st.warning("Need to be paid premium user")
    
else:
    st.header(f"Welcome, {st.experimental_user.name}!")
    col1, col2 = st.columns([1,10])

    col1.text("Your Resume Content")

    contact_tab, experience_tab, education_tab, skill_tab = col2.tabs(["Contact", "Professional Experience", "Education", "Professional Summary"])

    with contact_tab:
        contact_form()

    #TODO dynamic expander name
    with experience_tab:
        if st.button("Add Experience", "add_experience_button"):
            id = find_next_id("experience")

            document_title = f"experience_{id:02}"          

            create_firestore_document("experience", document_title)
            upload_firebase_db("experience",
                               document_title,
                               organization = None,
                               role = None
                               )
        generate_experience()
        

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

    with skill_tab:
        if st.button("Add Professional Summary", key = "add_skill_button"):
            id = find_next_id("summary")

            document_title = f"career_summary_{id:02}"

            create_firestore_document("summary", document_title)
            upload_firebase_db("summary",
                               document_title,
                               skill="",
                               description="")
        
        generate_summary()
