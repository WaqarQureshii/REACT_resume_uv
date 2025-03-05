import streamlit as st

from firebase_tools import upload_firebase_db, get_firestore_information


def contact_form() -> None:
    with st.form(key="contact_form", enter_to_submit=False, clear_on_submit=False):
        row1 = st.columns(2)
        firstname = row1[0].text_input('First Name',
                                        value = get_firestore_information("contact", "contact", "first_name"),
                                        placeholder="John",
                                        key="first_name")
        lastname = row1[1].text_input('Last Name',
                                        value = get_firestore_information("contact", "contact", "last_name"),
                                        placeholder='Doe',
                                        key="last_name")

        row2 = st.columns(2)
        email_address = row2[0].text_input('Email Address',
                                            value = get_firestore_information("contact", "contact", "email_address"),
                                            placeholder='johndoe@gmail.com',
                                            key="email_address")
        phone_number = row2[1].text_input('Phone Number',
                                            value = get_firestore_information("contact", "contact", "phone_number"),
                                            placeholder='+1 (123)-123-1234',
                                            key="phone_number")

        row3 = st.columns(2)
        linkedin_url = row3[0].text_input('LinkedIn URL',
                                            value = get_firestore_information("contact", "contact", "linkedin_url"),
                                            placeholder="https://linkedin.com/in/johndoe",
                                            key="linkedin_url")
        personal_website = row3[1].text_input('Personal Website URL',
                                                value = get_firestore_information("contact", "contact", "personal_website"),
                                                placeholder="https://personalwebsite.com",
                                                key="personalsite_url")

        row4 = st.columns(3)
        country = row4[0].text_input('Country',
                                        value = get_firestore_information("contact", "contact", "country"),
                                        placeholder="Canada",
                                        key="country")
        state = row4[1].text_input('State/Province',
                                    value = get_firestore_information("contact", "contact", "state"),
                                    placeholder="Ontario",
                                    key="state")
        city = row4[2].text_input('City',
                                    value = get_firestore_information("contact", "contact", "city"),
                                    placeholder="Toronto",
                                    key="city ")

        submitted_contact = st.form_submit_button("Submit")

        if submitted_contact:
            upload_firebase_db("contact",
                               "contact", 
                                first_name=firstname,
                                last_name = lastname,
                                email_address=email_address,
                                phone_number=phone_number,
                                linkedin_url=linkedin_url,
                                personal_website=personal_website,
                                country=country,
                                state=state,
                                city=city)

def experience_values(existing: bool, firestore_collection_name: str, firestore_document_name: str, firestore_field: str):
    if existing:
        return get_firestore_information(firestore_collection_name, firestore_document_name, firestore_field)
    else:
        return None

def existing_experience_form(id: int, existing_experience: bool) -> None:
    with st.form(f"experience_form_{id}"):
        row1 = st.columns([10,4,10])
        organization = row1[0].text_input(
            "Organization Name",
            value=experience_values(existing_experience, "current_experience", f"experience_{id}", "organization"),
            placeholder="ABC Corporation",
            key=f"organization_{id}")
        present = row1[1].checkbox("Present Role?",
                                   key=f"present_{id}")
        role = row1[2].text_input("Role at Organization",
                                  value=get_firestore_information("current_experience", f"experience_{id}", "role"),
                                  placeholder="Analyst",
                                  key=f"role_{id}")

        row2 = st.columns([1,1,3])
        start_date = row2[0].date_input("Start Date",
                                        value=get_firestore_information("current_experience", f"experience_{id}", "start_date"),
                                        key=f"start_date_{id}")
        if not present:
            end_date = row2[1].date_input("End Date",
                                          value=get_firestore_information("current_experience", f"experience_{id}", "end_date"),
                                          key=f"end_date_{id}")
        location = row2[2].text_input("Location",
                                      value=get_firestore_information("current_experience", f"experience_{id}", "location"),
                                      placeholder="Toronto, Canada",
                                      key=f"location_{id}")
        
        row3 = st.columns([3,3,10])
        experience_check1 = row3[0].checkbox("Include",
                                             value=get_firestore_information("current_experience", f"experience_{id}", "experience_check1"),
                                             key=f"experience_check1_{id}")
        experience_category1 = row3[1].text_area("Category",
                                                 value=get_firestore_information("current_experience", f"experience_{id}", "experience_category1"),
                                                 key=f"experience_category1_{id}",
                                                 placeholder="separate by commas")
        experience_textarea1 = row3[2].text_area("Experience",
                                                 value=get_firestore_information("current_experience", f"experience_{id}", "experience_textarea1"),
                                                 key=f"experience1_{id}",
                                                 placeholder="Bullet Pointed Experience")

        row4 = st.columns([3,3,10])
        experience_check2 = row4[0].checkbox("Include",
                                             value=get_firestore_information("current_experience", f"experience_{id}", "experience_check2"),
                                             key=f"experience_check2_{id}")
        experience_category2 = row4[1].text_area("Category",
                                                 value=get_firestore_information("current_experience", f"experience_{id}", "experience_category2"),
                                                 key=f"experience_category2_{id}",
                                                 placeholder="separate by commas")
        experience_textarea2 = row4[2].text_area("Experience",
                                                 value=get_firestore_information("current_experience", f"experience_{id}", "experience_textarea2"),
                                                 key=f"experience2_{id}",
                                                 placeholder="Bullet Pointed Experience")

        row5 = st.columns([3,3,10])
        experience_check3 = row5[0].checkbox("Include",
                                             value=get_firestore_information("current_experience", f"experience_{id}", "experience_check3"),
                                             key=f"experience_check3_{id}")
        experience_category3 = row5[1].text_area("Category",
                                                 value=get_firestore_information("current_experience", f"experience_{id}", "experience_category3"),
                                                 key=f"experience_category3_{id}",
                                                 placeholder="separate by commas")
        experience_textarea3 = row5[2].text_area("Experience",
                                                 value=get_firestore_information("current_experience", f"experience_{id}", "experience_textarea3"),
                                                 key=f"experience3_{id}",
                                                 placeholder="Bullet Pointed Experience")

        row6 = st.columns([3,3,10])
        experience_check4 = row6[0].checkbox("Include",
                                             value=get_firestore_information("current_experience", f"experience_{id}", "experience_check4"),
                                             key=f"experience_check4_{id}")
        experience_category4 = row6[1].text_area("Category",
                                                 value=get_firestore_information("current_experience", f"experience_{id}", "experience_category4"),
                                                 key=f"experience_category4_{id}",
                                                 placeholder="separate by commas")
        experience_textarea4 = row6[2].text_area("Experience",
                                                 value=get_firestore_information("current_experience", f"experience_{id}", "experience_textarea4"),
                                                 key=f"experience4_{id}",
                                                 placeholder="Bullet Pointed Experience")

        row7 = st.columns([3,3,10])
        experience_check5 = row7[0].checkbox("Include",
                                             value=get_firestore_information("current_experience", f"experience_{id}", "experience_check5"),
                                             key=f"experience_check5_{id}")
        experience_category5 = row7[1].text_area("Category",
                                                 value=get_firestore_information("current_experience", f"experience_{id}", "experience_category5"),
                                                 key=f"experience_category5_{id}",
                                                 placeholder="separate by commas")
        experience_textarea5 = row7[2].text_area("Experience",
                                                 value=get_firestore_information("current_experience", f"experience_{id}", "experience_textarea5"),
                                                 key=f"experience5_{id}",
                                                 placeholder="Bullet Pointed Experience")
        
        submitted = st.form_submit_button("Submit")
        if submitted:
            write_status = upload_firebase_db("current_experience")

def add_experience_form(id: int) -> None:
    with st.form(f"experience_form_{id}"):
        row1 = st.columns([10,4,10])
        organization = row1[0].text_input(
            "Organization Name",
            value = get_firestore_information("current_experience", f"experience_{id}", "organization"),
            placeholder="ABC Corporation",
            key=f"organization_{id}")
        present = row1[1].checkbox("Present Role?",
                                   key=f"present_{id}")
        role = row1[2].text_input("Role at Organization",
                                  value=get_firestore_information("current_experience", f"experience_{id}", "role"),
                                  placeholder="Analyst",
                                  key=f"role_{id}")

        row2 = st.columns([1,1,3])
        start_date = row2[0].date_input("Start Date",
                                        value=get_firestore_information("current_experience", f"experience_{id}", "start_date"),
                                        key=f"start_date_{id}")
        if not present:
            end_date = row2[1].date_input("End Date",
                                          value=get_firestore_information("current_experience", f"experience_{id}", "end_date"),
                                          key=f"end_date_{id}")
        location = row2[2].text_input("Location",
                                      value=get_firestore_information("current_experience", f"experience_{id}", "location"),
                                      placeholder="Toronto, Canada",
                                      key=f"location_{id}")
        
        row3 = st.columns([3,3,10])
        experience_check1 = row3[0].checkbox("Include",
                                             value=get_firestore_information("current_experience", f"experience_{id}", "experience_check1"),
                                             key=f"experience_check1_{id}")
        experience_category1 = row3[1].text_area("Category",
                                                 value=get_firestore_information("current_experience", f"experience_{id}", "experience_category1"),
                                                 key=f"experience_category1_{id}",
                                                 placeholder="separate by commas")
        experience_textarea1 = row3[2].text_area("Experience",
                                                 value=get_firestore_information("current_experience", f"experience_{id}", "experience_textarea1"),
                                                 key=f"experience1_{id}",
                                                 placeholder="Bullet Pointed Experience")

        row4 = st.columns([3,3,10])
        experience_check2 = row4[0].checkbox("Include",
                                             value=get_firestore_information("current_experience", f"experience_{id}", "experience_check2"),
                                             key=f"experience_check2_{id}")
        experience_category2 = row4[1].text_area("Category",
                                                 value=get_firestore_information("current_experience", f"experience_{id}", "experience_category2"),
                                                 key=f"experience_category2_{id}",
                                                 placeholder="separate by commas")
        experience_textarea2 = row4[2].text_area("Experience",
                                                 value=get_firestore_information("current_experience", f"experience_{id}", "experience_textarea2"),
                                                 key=f"experience2_{id}",
                                                 placeholder="Bullet Pointed Experience")

        row5 = st.columns([3,3,10])
        experience_check3 = row5[0].checkbox("Include",
                                             value=get_firestore_information("current_experience", f"experience_{id}", "experience_check3"),
                                             key=f"experience_check3_{id}")
        experience_category3 = row5[1].text_area("Category",
                                                 value=get_firestore_information("current_experience", f"experience_{id}", "experience_category3"),
                                                 key=f"experience_category3_{id}",
                                                 placeholder="separate by commas")
        experience_textarea3 = row5[2].text_area("Experience",
                                                 value=get_firestore_information("current_experience", f"experience_{id}", "experience_textarea3"),
                                                 key=f"experience3_{id}",
                                                 placeholder="Bullet Pointed Experience")

        row6 = st.columns([3,3,10])
        experience_check4 = row6[0].checkbox("Include",
                                             value=get_firestore_information("current_experience", f"experience_{id}", "experience_check4"),
                                             key=f"experience_check4_{id}")
        experience_category4 = row6[1].text_area("Category",
                                                 value=get_firestore_information("current_experience", f"experience_{id}", "experience_category4"),
                                                 key=f"experience_category4_{id}",
                                                 placeholder="separate by commas")
        experience_textarea4 = row6[2].text_area("Experience",
                                                 value=get_firestore_information("current_experience", f"experience_{id}", "experience_textarea4"),
                                                 key=f"experience4_{id}",
                                                 placeholder="Bullet Pointed Experience")

        row7 = st.columns([3,3,10])
        experience_check5 = row7[0].checkbox("Include",
                                             value=get_firestore_information("current_experience", f"experience_{id}", "experience_check5"),
                                             key=f"experience_check5_{id}")
        experience_category5 = row7[1].text_area("Category",
                                                 value=get_firestore_information("current_experience", f"experience_{id}", "experience_category5"),
                                                 key=f"experience_category5_{id}",
                                                 placeholder="separate by commas")
        experience_textarea5 = row7[2].text_area("Experience",
                                                 value=get_firestore_information("current_experience", f"experience_{id}", "experience_textarea5"),
                                                 key=f"experience5_{id}",
                                                 placeholder="Bullet Pointed Experience")
        
        submitted = st.form_submit_button("Submit")
        if submitted:
            write_status = upload_firebase_db("current_experience")