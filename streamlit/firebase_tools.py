from google.cloud import firestore
import streamlit as st
from google.cloud.firestore_v1.collection import CollectionReference

import datetime

def create_user_db(db: firestore.DocumentReference):
    # Instantiate User Document in Firestore
    db.set({
            "date_joined": datetime.datetime.now(),
            "fullname": st.experimental_user.name
        })


    # Instantiate Contact Document in Firestore
    contact_data = {
        "first_name": "",
        "last_name": "",
        "email_address": "",
        "phone_number": "",
        "linkedin_url": "",
        "personal_website": "",
        "country": "",
        "state": "",
        "city": ""
    }

    contact_collection = db.collection("contact")
    contact_collection.document("contact").set(contact_data)

    return db

def get_user_db() -> firestore.DocumentReference:
    db = firestore.Client.from_service_account_info(st.secrets["GOOGLE_APPLICATION_CREDENTIALS"]).collection("users").document(st.experimental_user.email)
    if db.get().to_dict():
        return db
    else:
        db = create_user_db(db)
    
    return db

def upload_firebase_db(firestore_collection_name: str, firestore_document_name:str, **fields: str|bool) -> None:
    """
    Uploads data to a specified Firestore document within a collection.

    This function retrieves the user's Firestore database reference and uploads
    the provided fields to a specified document within a specified collection.

    Args:
        firestore_collection_name (str): The name of the Firestore collection.
        firestore_document_name (str): The name of the Firestore document.
        **fields (str|bool): Key-value pairs representing the fields to be set
            in the Firestore document.

    Returns:
    None
    """
    db = get_user_db()
    document = db.collection(firestore_collection_name).document(firestore_document_name)
    document.set(fields)

def get_firestore_information(firestore_collection_name: str, firestore_document_name: str) -> dict:
    """Get information from the collection(users).document(email)"""
    db = get_user_db()
    document = db.collection(firestore_collection_name).document(firestore_document_name)
    information = document.get().to_dict()

    if information:
        return information
    else:
        information = {}
        return information

def get_firestore_collection(firestore_collection: str) -> CollectionReference:
    """
    Retrieve a Firestore collection reference for the specified collection name.

    This function uses the user's Firestore document reference to access a specific
    collection within the user's document.

    Args:
        firestore_collection (str): The name of the Firestore collection to retrieve.

    Returns:
        CollectionReference: A reference to the specified Firestore collection.
    """
    db = get_user_db()
    collection = db.collection(firestore_collection)
    return collection

def create_firestore_document(db: firestore.DocumentReference, firestore_collection_name: str, firestore_document_name: str):
    firestore_collection_name = db.collection("current_experience").document(firestore_document_name).set({})