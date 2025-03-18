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

def get_firestore_value(firestore_collection_name: str, firestore_document_name: str) -> dict:
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


def create_firestore_document(firestore_collection_name: str, firestore_document_name: str):
    db = get_user_db()
    firestore_collection_name = db.collection(firestore_collection_name).document(firestore_document_name).set({})


def delete_firestore_document(firestore_collection_name: str, firestore_document_name: str) -> None:
    db = get_user_db()
    db.collection(firestore_collection_name).document(firestore_document_name).delete()

def get_resume_formatted_for_llm(collection_type: str) -> str:
    user_db = get_user_db()
    collections = user_db.collection(collection_type)

    result = []

    for doc in collections.stream():
        data=doc.to_dict()
        
        if collection_type=="experience":
            # Retrieve the job name and other fields
            job_title = data.get("role", "UNKNOWN ROLE")
            company = data.get("organization", "UNKNOWN ORGANIZATION")
            start_date = data.get("start_date", "YYYY-MM")
            if data.get("present"):
                end_date = "Present"
            else:
                end_date = data.get("end_date", "YYYY-MM")

            work_location = data.get("location", "UNKNOWN LOCATION")

            experiences = [
                value for key, value in data.items()
                if key.startswith("experience_description") and value
            ]

            result.append(f"Title: {job_title}\n")
            result.append(f"Company: {company}\n")
            result.append(f"Start Date: {start_date}\n")
            result.append(f"End Date: {end_date}\n")
            result.append(f"Location: {work_location}\n")
            for experience in experiences:
                result.append(f"- {experience}")

        if collection_type == "summary":
            skill = data.get("skill", "Unknown Skill")
            skill_summary = data.get("description", "Unknown description")

            result.append(f"Skill: {skill}")
            result.append(skill_summary)

        if collection_type == "education":
            institution = data.get("institution", "Unknown institution")
            degree = data.get("degree", "Unknown degree")
            specialist = data.get("specialist", "Unknown")
            major = data.get("major", "Unknown")
            minor = data.get("minor", "Unknown")
            education_location = data.get("location", "Unknown")
            year_earned = data.get("year_earned", "Unknown")
            gpa = data.get("gpa", "Unknown")
            additional_info = data.get("additional_info", "Unknown")

            result.append(f"Institution: {institution}")
            result.append(f"Degree: {degree}, Specialist: {specialist}, Major: {major}, Minor: {minor}")
            result.append(f"Location: {education_location}")
            result.append(f"Year Earned: {year_earned}")
            result.append(f"Additional Info: {additional_info}")

        if collection_type == "contact":
            email_address = data.get("email_address", None)
            first_name = data.get("first_name", None)
            last_name = data.get("last_name", None)
            contact_linkedin_url = data.get("linkedin_url", None)
            phone_number = data.get("phone_number", None)
            personal_website = data.get("personal_website", None)

            result.append(f"Email Address: {email_address}")
            result.append(f"Name: {first_name} {last_name}")
            result.append(f"LinkedIN URL: {contact_linkedin_url}")
            result.append(f"Phone Number: {phone_number}")
            result.append(f"personal_website: {personal_website}")


    return "\n".join(result)