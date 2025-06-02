import streamlit as st
from langchain_openai import ChatOpenAI

from tools_general import login_user
from tools_langchain import run_chain
from tools_firebase import get_firestore_value
from tools_langchain import get_resume_information_in_list
from tools_langgraph import run_chatbot
from langchain.chat_models import init_chat_model

import os
os.environ["LANGSMITH_TRACING"] = st.secrets.langsmith.tracing
os.environ["LANGSMITH_ENDPOINT"] = st.secrets.langsmith.endpoint
os.environ["LANGSMITH_API_KEY"] = st.secrets.langsmith.api_key
os.environ["LANGSMITH_PROJECT"] = st.secrets.langsmith.project

if not st.experimental_user.is_logged_in:
    login_user()

elif not get_firestore_value("subscription_status", "subscription_status").get("premium"):
    st.warning("Need to be paid premium user")

else:
    st.header(f"Create your resume, {st.experimental_user.name} by following the easy steps below!")

    col1, col2, col3, col4 = st.columns(4)

    llm_selection = col1.pills(
        "LLM selection",
        options = ['OpenAI', 'Google Gemini'],
        selection_mode="single",
        default="OpenAI"
    )

    model_options = {
        "OpenAI": {"langchain_model": "OpenAI",
                   "options": ["o4-mini-2025-04-16", "o3-mini-2025-01-31", "gpt-4.1-mini-2025-04-14", "gpt-4.1-nano-2025-04-14"]},
        "Google Gemini": {"langchain_model": "GoogleGemini",
                          "options": ["gemini-1.5-pro", "gemini-2.0-flash", "gemini-2.0-flash-lite", "gemini-2.5-pro-exp-03-25"]}
    }


    model_selection = col2.selectbox(f"Select which model of {llm_selection}",
                                  options=model_options[llm_selection]['options'],
                                  index=1,
                                  key="model_selection")
    
    job_posting = st.text_area("Input your job description", height=300, key="job_posting")
    
    if job_posting:
        if llm_selection == "OpenAI":
            api_key = st.secrets.llm_keys.openai_key
        elif llm_selection == "Google Gemini":
            api_key = st.secrets.llm_keys.google_gemini_key
        llm = init_chat_model(model=model_selection, api_key=api_key)
        run_chatbot()