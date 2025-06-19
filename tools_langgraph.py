from langgraph.prebuilt import create_react_agent
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from tools_firebase import get_user_information
from langchain_openai import ChatOpenAI
from langgraph.graph.graph import CompiledGraph
from langsmith import traceable


from typing import Literal

import os
from pydantic_models import ProfessionalSummary, ContactInformation, WorkExperience, Education, ResumeState

os.environ["LANGCHAIN_PROJECT"] = st.secrets.langsmith.project
os.environ["LANGCHAIN_API_KEY"] = st.secrets.langsmith.api_key
os.environ["LANGCHAIN_ENDPOINT"] = st.secrets.langsmith.endpoint
os.environ["LANGCHAIN_TRACING_V2"] = st.secrets.langsmith.tracing


def get_user_info(collection_type: Literal["experience", "summary", "education", "contact"], state: ResumeState) -> ResumeState:
        """Fetches user information from the firestore database based on the collection type provided.
        
        Args:
            collection_type (Literal["experience", "summary", "education", "contact"]): The type of collection to fetch user information from.
            "experience" for work experience
            "summary" for professional summary
            "education" for education qualifications
            "contact" for basic contact information
        """

        data = get_user_information(collection_type)

        if collection_type == "experience":
            if state.user_work_experience:
                return {state.user_work_experience: state.user_work_experience}
            else:
                {state.user_work_experience: [WorkExperience(**exp) for exp in data]}
        
        if collection_type == "summary":
            if state.user_professional_summary:
                return {state.user_professional_summary: state.user_professional_summary}
            else:
                {state.user_professional_summary: [ProfessionalSummary(**skill) for skill in data]}

        if collection_type == "education":
            if state.user_education:
                return {state.user_education: state.user_education}
            else:
                return {state.user_education: Education(**data)}

        if collection_type == "contact":
            if state.contact_information:
                return {state.contact_information: state.contact_information}
            else:
                return {state.contact_information: ContactInformation(**data)}
        


def create_graph(llm: Literal["OpenAI", "Google Gemini"], llm_model: str) -> CompiledGraph:
    if llm == "OpenAI":
        model = ChatOpenAI(model=llm_model,
                           api_key=st.secrets.llm_keys.openai_key)
    else:
        model = ChatGoogleGenerativeAI(model=llm_model,
                                       api_key=st.secrets.llm_keys.google_gemini_key)
    resource_agent = create_react_agent(
        model=model,
        tools=[get_user_info],
        prompt = ("You are a helpful assistant to a resume builder. You are capable of extracting and getting relevant information and are equipped with tools to gather user's information and store them, as well as accessing analysis completed by another agent."),
        name="resource_agent",
        response_format=ResumeState
    )

    return resource_agent