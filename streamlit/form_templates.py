import streamlit as st

from firebase_tools import upload_firebase_db, get_firestore_value, delete_firestore_document


def contact_form() -> None:
    with st.form(key="contact_form", enter_to_submit=False, clear_on_submit=False):
        document_dict = get_firestore_value("contact", "contact")
        row1 = st.columns(2)
        firstname = row1[0].text_input('First Name',
                                        value = document_dict.get("first_name",None),
                                        placeholder="John",
                                        key="first_name")
        lastname = row1[1].text_input('Last Name',
                                        value = document_dict.get("last_name",None),
                                        placeholder='Doe',
                                        key="last_name")

        row2 = st.columns(2)
        email_address = row2[0].text_input('Email Address',
                                            value = document_dict.get("email_address",None),
                                            placeholder='johndoe@gmail.com',
                                            key="email_address")
        phone_number = row2[1].text_input('Phone Number',
                                            value = document_dict.get("phone_number",None),
                                            placeholder='+1 (123)-123-1234',
                                            key="phone_number")

        row3 = st.columns(2)
        linkedin_url = row3[0].text_input('LinkedIn URL',
                                            value = document_dict.get("linkedin_url",None),
                                            placeholder="https://linkedin.com/in/johndoe",
                                            key="linkedin_url")
        personal_website = row3[1].text_input('Personal Website URL',
                                                value = document_dict.get("personal_website",None),
                                                placeholder="https://personalwebsite.com",
                                                key="personalsite_url")

        row4 = st.columns(3)
        country = row4[0].text_input('Country',
                                        value = document_dict.get("country",None),
                                        placeholder="Canada",
                                        key="country")
        state = row4[1].text_input('State/Province',
                                    value = document_dict.get("state",None),
                                    placeholder="Ontario",
                                    key="state")
        city = row4[2].text_input('City',
                                    value = document_dict.get("city",None),
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


def experience_form(id: int, existing_experience: bool) -> None:
    id = f"{id:02}"
    document_dict = get_firestore_value("current_experience", f"experience_{id}")
    with st.form(f"experience_form_{id}"):
        row1 = st.columns([10,4,10])
        organization = row1[0].text_input(
            "Organization Name",
            value = document_dict.get("organization",None),
            placeholder="ABC Corporation",
            key=f"organization_{id}")
        present = row1[1].checkbox("Present Role?",
                                   key=f"present_{id}")
        role = row1[2].text_input("Role at Organization",
                                  value = document_dict.get("role",None),
                                  placeholder="Analyst",
                                  key=f"role_{id}")

        row2 = st.columns([1,1,3])
        start_date = row2[0].date_input("Start Date",
                                        value = document_dict.get("start_date",None),
                                        key=f"start_date_{id}")
        if not present:
            end_date = row2[1].date_input("End Date",
                                          value = document_dict.get("end_date",None),
                                          key=f"end_date_{id}")
        location = row2[2].text_input("Location",
                                      value = document_dict.get("location",None),
                                      placeholder="Toronto, Canada",
                                      key=f"location_{id}")
        
        row3 = st.columns([4,10])
        experience_category1 = row3[0].text_area("Category",
                                                 value = document_dict.get("experience_category1",None),
                                                 key=f"experience_category1_{id}",
                                                 placeholder="separate by commas")
        experience_textarea1 = row3[1].text_area("Experience",
                                                 value = document_dict.get("experience_textarea1",None),
                                                 key=f"experience1_{id}",
                                                 placeholder="Bullet Pointed Experience")

        row4 = st.columns([4,10])
        experience_category2 = row4[0].text_area("Category",
                                                 value=document_dict.get("experience_category2",None),
                                                 key=f"experience_category2_{id}",
                                                 placeholder="separate by commas")
        experience_textarea2 = row4[1].text_area("Experience",
                                                 value=document_dict.get("experience_textarea2",None),
                                                 key=f"experience2_{id}",
                                                 placeholder="Bullet Pointed Experience")

        row5 = st.columns([4,10])
        experience_category3 = row5[0].text_area("Category",
                                                 value=document_dict.get("experience_category3",None),
                                                 key=f"experience_category3_{id}",
                                                 placeholder="separate by commas")
        experience_textarea3 = row5[1].text_area("Experience",
                                                 value=document_dict.get("experience_textarea3",None),
                                                 key=f"experience3_{id}",
                                                 placeholder="Bullet Pointed Experience")

        row6 = st.columns([4,10])
        experience_category4 = row6[0].text_area("Category",
                                                 value=document_dict.get("experience_category4",None),
                                                 key=f"experience_category4_{id}",
                                                 placeholder="separate by commas")
        experience_textarea4 = row6[1].text_area("Experience",
                                                 value=document_dict.get("experience_textarea4",None),
                                                 key=f"experience4_{id}",
                                                 placeholder="Bullet Pointed Experience")

        row7 = st.columns([4,10])
        experience_category5 = row7[0].text_area("Category",
                                                 value=document_dict.get("experience_category5",None),
                                                 key=f"experience_category5_{id}",
                                                 placeholder="separate by commas")
        experience_textarea5 = row7[1].text_area("Experience",
                                                 value=document_dict.get("experience_textarea5",None),
                                                 key=f"experience5_{id}",
                                                 placeholder="Bullet Pointed Experience")
        
        row8 = st.columns([1,1,10])
        submitted = row8[0].form_submit_button("Submit", type="primary")
        if submitted:
            upload_firebase_db("current_experience",
                               f"experience_{id}",
                               organization=organization,
                               present=present,
                               role=role,
                               start_date=start_date,
                               end_date=end_date,
                               location=location,
                               experience_category1=experience_category1,
                               experience_description1=experience_textarea1,
                               experience_category2=experience_category2,
                               experience_description2=experience_textarea2,experience_category3=experience_category3,
                               experience_description3=experience_textarea3,
                               experience_category4=experience_category4,
                               experience_description4=experience_textarea4,
                               experience_category5=experience_category5,
                               experience_description5=experience_textarea5)
            
        if existing_experience:
            delete_option = row8[1].form_submit_button("Delete", type="secondary")
            if delete_option:
                delete_firestore_document("current_experience", f"experience_{id}")
                st.switch_page("content/4_your_content.py")