import streamlit as st

from tools_firebase import upload_firebase_db, get_firestore_value, delete_firestore_document


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
    document_dict = get_firestore_value("experience", f"experience_{id}")
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
        start_date = row2[0].text_input("Start Date",
                                        value = document_dict.get("start_date",None),
                                        key=f"start_date_{id}",
                                        placeholder="YYYY/MM")
        if not present:
            end_date = row2[1].text_input("End Date",
                                          value = document_dict.get("end_date",None),
                                          key=f"end_date_{id}",
                                          placeholder="YYYY/MM")
        else:
            end_date = None
            
        location = row2[2].text_input("Location",
                                      value = document_dict.get("location",None),
                                      placeholder="Toronto, Canada",
                                      key=f"job_location_{id}")
        
        row3 = st.columns([4,10])
        experience_category1 = row3[0].text_area("Category",
                                                 value = document_dict.get("experience_category1",None),
                                                 key=f"experience_category1_{id}",
                                                 placeholder="separate by commas")
        experience_textarea1 = row3[1].text_area("Experience",
                                                 value = document_dict.get("experience_description1",None),
                                                 key=f"experience1_{id}",
                                                 placeholder="Bullet Pointed Experience")

        row4 = st.columns([4,10])
        experience_category2 = row4[0].text_area("Category",
                                                 value=document_dict.get("experience_category2",None),
                                                 key=f"experience_category2_{id}",
                                                 placeholder="separate by commas")
        experience_textarea2 = row4[1].text_area("Experience",
                                                 value=document_dict.get("experience_description2",None),
                                                 key=f"experience2_{id}",
                                                 placeholder="Bullet Pointed Experience")

        row5 = st.columns([4,10])
        experience_category3 = row5[0].text_area("Category",
                                                 value=document_dict.get("experience_category3",None),
                                                 key=f"experience_category3_{id}",
                                                 placeholder="separate by commas")
        experience_textarea3 = row5[1].text_area("Experience",
                                                 value=document_dict.get("experience_description3",None),
                                                 key=f"experience3_{id}",
                                                 placeholder="Bullet Pointed Experience")

        row6 = st.columns([4,10])
        experience_category4 = row6[0].text_area("Category",
                                                 value=document_dict.get("experience_category4",None),
                                                 key=f"experience_category4_{id}",
                                                 placeholder="separate by commas")
        experience_textarea4 = row6[1].text_area("Experience",
                                                 value=document_dict.get("experience_description4",None),
                                                 key=f"experience4_{id}",
                                                 placeholder="Bullet Pointed Experience")

        row7 = st.columns([4,10])
        experience_category5 = row7[0].text_area("Category",
                                                 value=document_dict.get("experience_category5",None),
                                                 key=f"experience_category5_{id}",
                                                 placeholder="separate by commas")
        experience_textarea5 = row7[1].text_area("Experience",
                                                 value=document_dict.get("experience_description5",None),
                                                 key=f"experience5_{id}",
                                                 placeholder="Bullet Pointed Experience")
        
        row8 = st.columns([1,1,10])
        submitted = row8[0].form_submit_button("Submit", type="primary")
        if submitted:
            upload_firebase_db("experience",
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
                delete_firestore_document("experience", f"experience_{id}")
                st.switch_page("content/4_your_content.py")


def education_form(id: int, existing_education: bool) -> None:
    id = f"{id:02}"
    document_dict = get_firestore_value("education", f"education_{id}")
    with st.form(f"education_{id}"):
        row1 = st.columns(2)
        degree = row1[0].text_input(
            "Degree, Diploma, Certificate Name",
            value=document_dict.get("degree", None),
            placeholder="B. Comm: Economics Major",
            key=f"degree_{id}"
        )
        institution = row1[1].text_input(
            "Institution Name?",
            value = document_dict.get("institution", None),
            placeholder="Queens University",
            key=f"institution_{id}"
        )

        row2=st.columns(2)
        location = row2[0].text_input(
            "Location",
            value=document_dict.get("location", None),
            placeholder="Kingston, ON, Canada",
            key=f"education_location_{id}"
        )
        year_earned = row2[1].text_input("Year qualification was earned in",
                                         value=document_dict.get("year_earned", None),
                                         placeholder="YYYY",
                                         key=f"year_earned_{id}"
                                         )
        
        row3=st.columns(3)
        specialist = row3[0].text_input("Specialization",
                                        value=document_dict.get("specialist", None),
                                        placeholder="Accounting Specialist",
                                        key=f"specialist_{id}"
                                        )
        major = row3[1].text_input("Major",
                                   value=document_dict.get("major",None),
                                   placeholder="Economics Major",
                                   key=f"major_{id}")
        minor = row3[2].text_input("Minor",
                                   value=document_dict.get("minor", None),
                                   placeholder="English Minor",
                                   key=f"minor_{id}"
                                   )
        
        row4=st.columns([1,5])
        gpa = row4[0].text_input("GPA (if applicable)",
                                 value=document_dict.get("gpa", None),
                                 placeholder="3.9",
                                 key=f"gpa_{id}"
                                 )
        additional_info = row4[1].text_input("Additional Information",
                                             value=document_dict.get("additional_info", None),
                                             placeholder="Graduated with Distinction",
                                             key=f"additional_info_{id}")
        
        row5 = st.columns([1,1,10])
        submitted = row5[0].form_submit_button("Submit", type="primary")
        if submitted:
            upload_firebase_db("education",
                               f"education_{id}",
                               degree=degree,
                               institution=institution,
                               location=location,
                               year_earned=year_earned,
                               specialist=specialist,
                               major=major,
                               minor=minor,
                               gpa=gpa,
                               additional_info=additional_info)
            
        if existing_education:
            delete_option = row5[1].form_submit_button("Delete", type="secondary")
            if delete_option:
                delete_firestore_document("education", f"education_{id}")
                st.switch_page("content/4_your_content.py")


def summary_form(id: int, existing_summary: bool) -> None:
    id = f"{id:02}"
    document_dict = get_firestore_value("summary", f"career_summary_{id}")
    with st.form(f"career_summary_form_{id}"):
        row1 = st.columns([4,10])
        summary_category1 = row1[0].text_area("Professional Skill/Achievement",
                                              value=document_dict.get("skill", None),
                                              key=f"skill_{id}",
                                              placeholder="Financial and Product Management")
        summary_1 = row1[1].text_area("Description",
                                      value=document_dict.get("description", None),
                                      key=f"summary_{id}",
                                      placeholder="7+ years managing full-cycle financial budgeting of over $100M+, forecasting significant risks and opportunities within the market, and assessing headcount resources for a 5,000+ headcount organization. 3+ years with a minimum of 3 direct reports owning various business unit portfolios.")
        
        row2 = st.columns([1,1,10])
        submitted = row2[0].form_submit_button("Submit", type = "primary")
        if submitted:
            upload_firebase_db("summary",
                               f"career_summary_{id}",
                               skill=summary_category1,
                               description=summary_1)
        
        if existing_summary:
            delete_option = row2[1].form_submit_button("Delete", type="secondary")
            if delete_option:
                delete_firestore_document("summary", f"career_summary_{id}")
                st.switch_page("content/4_your_content.py")