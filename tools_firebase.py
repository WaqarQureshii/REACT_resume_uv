from google.cloud import firestore
import streamlit as st
from google.cloud.firestore_v1.collection import CollectionReference
from typing import Literal, Union

import datetime

def create_user_db(db: firestore.DocumentReference):
    # Instantiate User Document in Firestore
    
    print("Running from create_user_db (firebase tools)")
    print(st.experimental_user.email)
    print("")
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

    subscription_status_collection = db.collection("subscription_status")
    subscription_status_collection.document("subscription_status").set({"premium": False})

    return db

def get_user_db() -> firestore.DocumentReference:
    user_email = st.experimental_user["email"]
    db = firestore.Client.from_service_account_info(st.secrets["GOOGLE_APPLICATION_CREDENTIALS"]).collection("users").document(user_email)
    if db.get().to_dict():
        return db
    else:
        db = create_user_db(db)
    
    return db

def upload_firebase_db(firestore_collection_name: str, firestore_document_name:str, **fields: str|bool) -> dict:
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

def get_resume_formatted_for_llm(collection_type: Literal["experience", "summary", "education", "contact"]) -> str:
    Candidate_db = get_user_db()
    collections = Candidate_db.collection(collection_type)

    result = []  # Holds properly formatted job experience blocks
    
    for doc in collections.stream():
        data = doc.to_dict()
        
        if collection_type == "experience":
            # Retrieve primary job details
            job_title = data.get("role", "UNKNOWN ROLE")
            company = data.get("organization", "UNKNOWN ORGANIZATION")
            start_date = data.get("start_date", "YYYY-MM")
            job_linkedin_url = data.get("linkedin_url", "None")
            end_date = "Present" if data.get("present") else data.get("end_date", "YYYY-MM")
            work_location = data.get("location", "UNKNOWN LOCATION")

            # Retrieve experience descriptions
            experiences = [f"- {value}" for key, value in data.items() if key.startswith("experience_description") and value]

            # Group the full job experience into one block
            job_experience_block = "\n".join([
                f"**Title:** {job_title}",
                f"**Company:** {company}",
                f"**LinkedIn URL:** {job_linkedin_url}",
                f"**Start Date:** {start_date} | **End Date:** {end_date}",
                f"**Location:** {work_location}",
                "\n".join(experiences)  # Add experience descriptions
            ])

            result.append(job_experience_block)

        if collection_type == "summary":
            skill = data.get("skill", "Unknown Skill")
            skill_summary = data.get("description", "Unknown description")

            result.append(f"Skill: {skill}")
            result.append(skill_summary)

        if collection_type == "education":
            institution = data.get("institution", "Unknown institution")
            degree = data.get("degree", "Unknown degree")
            education_url = data.get("website_url", "None")
            specialist = data.get("specialist", "Unknown")
            major = data.get("major", "Unknown")
            minor = data.get("minor", "Unknown")
            education_location = data.get("location", "Unknown")
            year_earned = data.get("year_earned", "Unknown")
            gpa = data.get("gpa", "Unknown")
            additional_info = data.get("additional_info", "Unknown")

            result.append(f"Institution: {institution}")
            result.append(f"Degree: {degree}, Specialist: {specialist}, Major: {major}, Minor: {minor}")
            result.append(f"Website URL: {education_url}\n")
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


    return "\n\n".join(result).strip()

def get_user_information(collection_type: Literal["experience", "summary", "education", "contact"]) -> Union[list[dict], dict]:
    """Fetches user information from the firestore database based on the collection type provided.
    
    Args:
        collection_type (Literal["experience", "summary", "education", "contact"]): The type of collection to fetch user information from.
        "experience" for work experience
        "summary" for professional summary
        "education" for education qualifications
        "contact" for basic contact information

    Return (ResumeState)
    """

    Candidate_db = get_user_db()
    collections = Candidate_db.collection(collection_type)

    output_dict = []

    for doc in collections.stream():
        
        data = doc.to_dict()
        
        if collection_type == "experience":
            experiences = [f"- {value}" for key, value in data.items() if key.startswith("experience_description") and value]
            
            item = {
                "organization_name": data.get("organization", "User did not input organization name."),
                "linked_in_url": data.get("linkedin_url", "User did not input LinkedIN URL."),
                "job_location": data.get("location", "User did not input job location."),
                "job_title": data.get("role", "User did not input job title."),
                "start_date": data.get("start_date", "User did not input start date."),
                "end_date": data.get("end_date", "User did not input end date."),
                "present_role": data.get("present"),
                "responsibilities": experiences if experiences else "User did not input any experiences"
            }
            output_dict.append(item)


        if collection_type == "summary":
            skill_or_achievement = data.get("skill", "User did not provide a skill/achievement.")
            summary = data.get("description", "User did not provide a summary or description.")
            entry = skill_or_achievement + ": " + summary

            item = {
                "skill_and_summary": entry
            }
            output_dict.append(item)


        if collection_type == "education":
            item = {
                "degree_or_diploma_name": data.get("degree", "User did not input a degree or deploma name."),
                "institution_name": data.get("institution", "User did not input an institution name."),
                "year_earned": data.get("year_earned", "User did not input the year it was earned."),
                "location": data.get("location", "User did not input the location of the institution."),
                "specialization": data.get("specialist", "User did not input a specialization."),
                "major": data.get("major", "User did not input a major."),
                "minor": data.get("minor", "User did not input a minor."),
                "additional_info": data.get("additional_info", "User did not input any additional information.")
            }
            output_dict.append(item)
            

        if collection_type == "contact":
            item = {
                "first_name": data.get("first_name", "User did not input their first name."),
                "last_name": data.get("last_name", "User did not input their last name."),
                "email": data.get("emaiL_address", "User did not input their email address."),
                "contact_linkedin_url": data.get("linkedin_url", "User did not provide their LinkedIN URL."),
                "phone_number": data.get("phone_number", "User did not provider their phone number."),
                "personal_website": data.get("personal_website", "User did not provide their personal website."),
                "country": data.get("country", "User did not provide their residential country."),
                "state_province": data.get("state", "User did not provide their residential province/state."),
                "city": data.get("city", "User did not provide their residential city.")
            }
            output_dict = item


    return output_dict