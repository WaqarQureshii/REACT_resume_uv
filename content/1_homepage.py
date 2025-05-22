import streamlit as st
import time
from tools_general import login_user

st.title("Homepage")
st.subheader("Elevate your Resume with REACT")

homepage_copy = """
Your resume should work for you—not the other way around. With REACT, you can securely store your professional information and let our intelligent tool optimize it for every job application. Simply paste your desired job description, and REACT will tailor your resume with:
- Impactful **career taglines** to grab attention
- A refined :red[**professional summary**] that aligns with the role
- A clear :red[**summary of skills**], highlighting your strengths
- Customized :red[**work experience details**], emphasizing relevant achievements
- :red[**ATS-friendly**] formatting to boost visibility in hiring systems
- :red[**AI-generated cover letters and hiring manager messages**] to help you stand out

"""

def stream_copy():
    for word in homepage_copy.split(" "):
        yield word + " "
        time.sleep(0.02)

st.write_stream(stream_copy)
st.write("""Take control of your career trajectory. :red[**Make every application count with REACT**]. Find out what makes REACT different from other resume builders:""")
st.link_button("Learn more about REACT", "/about_react", type="secondary")

if not st.experimental_user.is_logged_in:
    if st.button("""💡 Sign in with your Google Account to get started!""", type="primary"):
        login_user()
else:
    st.link_button("""💡 View your account and revamp your information!""", "/your_content", type="primary")