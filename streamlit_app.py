import streamlit as st

from dependencies import sidebar_account

st.set_page_config(layout="wide")

# --- PAGE SETUP ---
home_page = st.Page(
    page="content/1_homepage.py",
    title="Home",
    icon=":material/home:",
    default = True
)

about_react = st.Page(
    page="content/2_about_react.py",
    title="What REACT does differently",
    icon=":material/info:"
)

your_content = st.Page(
    page="content/4_your_content.py",
    title="Your Content",
    icon=":material/content_copy:"
)

create_resume = st.Page(
    page="content/5_create_resume.py",
    title="Create Resume",
    icon=":material/stylus_note:"
)

# --- NAVIGATION SETUP ---
pg = st.navigation(
    {
        "About": [home_page, about_react],
        "REACT": [your_content, create_resume]
    }
)


# --- RUN NAVIGATION ---
pg.run()
sidebar_account()
