import streamlit as st
from langchain_openai import ChatOpenAI

from tools_general import login_user
from tools_llm import get_resume_formatted_for_llm, get_openai_response

if not st.experimental_user.is_logged_in:
    login_user()

else:
    st.header(f"Create your resume, {st.experimental_user.name} by following the easy steps below!")

    col1, col2, col3, col4 = st.columns(4)

    llm_selection = col1.pills(
        "LLM selection",
        options = ['OpenAI', "Google Gemini"],
        selection_mode="single",
        default="OpenAI"
    )

    model_options = {
        "OpenAI": {"langchain_model": "OpenAI",
                   "options": ["o3-mini-2025-01-31", "gpt-4o-2024-08-06", "o1-mini-2024-09-12", "o1-2024-12-17"]},
        "Google Gemini": {"langchain_model": "GoogleGemini",
                          "options": ["gemini-1.5-pro", "gemini-2.0-flash", "gemini-2.0-flash-lite", "gemini-2.0-flash"]}
    }

    model_selection = col2.selectbox(f"Select which model of {llm_selection}",
                                  options=model_options[llm_selection]['options'],
                                  index=0,
                                  key="model_selection")

    desired_max_pages = col3.number_input("Maximum Pages to output", min_value=1, value="min", step=1, key="desired_pages")

    job_description = st.text_area("Input your job description", height=300)
    
    if st.button("Create Resume", key="create_resume", type="primary"):
        get_openai_response(model_options[llm_selection]['langchain_model'], model_selection, job_description)