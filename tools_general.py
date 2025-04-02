import streamlit as st

from tools_firebase import get_user_db, get_firestore_collection
from form_templates import experience_form, education_form, summary_form

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

def create_education_ui(id: int, existing_education: bool, title: Optional[str]=""):
    with st.expander(f"Education #{f"{id:02}"} {title}"):
        education_form(id, existing_education)


def create_summary_ui(id: int, existing_summary: bool, title: Optional[str]=""):
    with st.expander(f"{title} summary #{id}"):
        summary_form(id, existing_summary)


### --- Global Functions --- ###

def login_user():
    st.login()

def get_number_of_existing_experiences() -> int:
    collection = get_firestore_collection("experience")
    no_of_documents = collection.count().get()[0][0].value

    return int(no_of_documents)

def generate_experience():
    """
    Generate and display current experience entries from a Firestore collection.

    This function retrieves documents from the "experience" Firestore collection
    and creates an experience entry for each document using the `create_experience_ui` function.
    Each entry is displayed with its role and organization. If there are no documents in
    the collection, the function returns None.

    Returns:
        str: None if no documents are found, otherwise the function does not return a value.
    """
    experience_collection = get_firestore_collection("experience")
    if not any(experience_collection.stream()):
        return None
    
    for doc in experience_collection.stream():

        doc_dict = doc.to_dict()
        
        role = doc_dict.get("role", "")
        organization = doc_dict.get("organization", "")
        
        at_string = "@" if organization else ""
        title = f"{role} {at_string} {organization}"
        
        id_int = int(doc.id.split("_")[-1])

        create_experience_ui(id=id_int, existing_experience=True, title=title)

def find_next_id(collection_name: str) -> int:
    collection = get_firestore_collection(collection_name)
    # Fetch all document IDs from the collection
    doc_ids = [int(doc.id.split("_")[-1]) for doc in collection.stream()]

    if not doc_ids:
        return 1
    
    # Sort the IDs to check for gaps
    doc_ids.sort()
    
    # Find the first missing ID
    for idx, doc_id in enumerate(doc_ids, start=1):
        if doc_id != idx:
            return idx  # Return the first missing ID
    
    # If no gaps, return the next largest ID
    return doc_ids[-1] + 1


def generate_education():
    """
    Generate and display education entries from a Firestore collection.

    This function retrieves documents from the "education" Firestore collection
    and creates an experience entry for each document using the `create_education_ui` function.
    If there are no documents in the collection, the function returns None.

    Returns:
        str: None if no documents are found, otherwise the function does not return a value.
    """
    education_collection = get_firestore_collection("education")
    if not any(education_collection.stream()):
        return None
    
    for doc in education_collection.stream():

        doc_dict = doc.to_dict()
        
        degree = doc_dict.get("degree", "")
        institution = doc_dict.get("institution", "")
        
        at_string = "@" if institution else ""
        title = f"{degree} {at_string} {institution}"
        
        id_int = int(doc.id.split("_")[-1])

        create_education_ui(id=id_int, existing_education=True, title=title)


def generate_summary():
    """
    Generate and display summary entries from a Firestore collection.

    This function retrieves documents from the "summary" Firestore collection
    and creates an experience entry for each document using the `create_summary_ui` function.
    If there are no documents in the collection, the function returns None.

    Returns:
        str: None if no documents are found, otherwise the function does not return a value.
    """
    summary_collection = get_firestore_collection("summary")
    if not any(summary_collection.stream()):
        return None
    
    for doc in summary_collection.stream():

        doc_dict = doc.to_dict()

        skill = doc_dict.get("skill", "")
        summary = doc_dict.get("description")

        title = f"{skill}"
        id_int = int(doc.id.split("_")[-1])

        create_summary_ui(id=id_int, existing_summary = True, title=title)