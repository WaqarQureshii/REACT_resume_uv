from typing import Annotated, Literal, TypedDict
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langchain.chat_models import init_chat_model
from pydantic import BaseModel, Field
import streamlit as st

llm = init_chat_model(model="o3-mini-2025-01-31", api_key=st.secrets.llm_keys.openai_key)

class ActionClassifier(BaseModel):
    action_type: Literal["analyze job description",
                         "analyze candidate against job description",
                         "create perfect professional summary",
                         "create perfect work experiences",
                         "create perfect career taglines",
                         "create perfect summary of skills",
                         "revise candidate's professional summary",
                         "revise candidate's work experiences",
                         "create candidate's cover letter",
                         "create candidate's message to hiring manager",
                         "revise entire resume"] = Field(..., description="Which action to take for the candidate")
    action_confidence: int = Field(..., description="Confidence of the action type classification on a scale of 1 to 10, 10 being the highest confidence")
    scope_selection: Literal["Specific Section", "Entire Section"]
    scope_confidence: int = Field(..., description="Confidence of the scope selection on a scale of 1 to 10, 10 being the highest confidence")


class State(TypedDict):
    messages: Annotated[list, add_messages]
    action_type: str | None
    action_confidence: int | None
    scope_selection: str | None
    scope_confidence: int | None
    jd_analysis: str | None
    candidate_vs_jd_analysis: str | None
    ai_professional_summary: str | None
    ai_work_experiences: str | None
    ai_career_taglines: str | None
    ai_summary_of_skills: str | None
    revised_professional_summary: str | None
    revised_work_experiences: str | None
    ai_cover_letter: str | None
    ai_hiring_manager_message: str | None

def node_analyze_candidate_vs_jd(state: State):
    pass

def classify_message(state: State):
    print("Running classify_message")
    
    last_message = state["messages"][-1]
    classifier_llm = llm.with_structured_output(ActionClassifier)
    result = classifier_llm.invoke([
        {
            "role": "system",
            "content": """You have 2 jobs to complete. First job is to classify the type of action the user is asking for. It can be either:
            1. analyze job description
            2. analyze candidate against job description
            3. create perfect professional summary
            4. create perfect work experiences
            5. create perfect career taglines
            6. create perfect summary of skills
            7. revise candidate's professional summary
            8. revise candidate's work experiences
            9. create candidate's cover letter
            10. create candidate's message to hiring manager
            11. revise entire resume
            
            Related to the first job, you will rate the confidence of your answer on a scale of 1 to 10, where 10 is the highest confidence.
            
            The second job is to classify the scope of the resume an action is to be taken upon. It can be either:
            1. Specific Section
            2. Entire Section
            
            Related to the second job, you will rate the confidence of your answer on the scope of the action on a scale of 1 to 10, where 10 is the highest confidence."""
         },
         {"role": "user",
          "content": last_message.content}
    ])

    return {"action_type": result.action_type, "action_confidence": result.action_confidence, "scope_selection": result.scope_selection, "scope_confidence": result.scope_confidence}

def action_router(state: State):
    
    if state.get("jd_analysis") is None:
        pass
    elif state.get("action_type") == "analyze job description":
        # Placeholder for job description analysis logic
        state["jd_analysis"] = "Job description analysis result"
    elif state.get("action_type") == "analyze candidate against job description":
        # Placeholder for candidate vs job description analysis logic
        state["candidate_vs_jd_analysis"] = "Candidate vs JD analysis result"
    elif state.get("action_type") == "create perfect professional summary":
        # Placeholder for creating professional summary logic
        state["ai_professional_summary"] = "AI generated professional summary"
    elif state.get("action_type") == "create perfect work experiences":
        # Placeholder for creating work experiences logic
        state["ai_work_experiences"] = "AI generated work experiences"
    elif state.get("action_type") == "create perfect career taglines":
        # Placeholder for creating career taglines logic
        state["ai_career_taglines"] = "AI generated career taglines"
    elif state.get("action_type") == "create perfect summary of skills":
        # Placeholder for creating summary of skills logic
        state["ai_summary_of_skills"] = "AI generated summary of skills"
    elif state.get("action_type") == "revise candidate's professional summary":
        # Placeholder for revising professional summary logic
        state["revised_professional_summary"] = "Revised professional summary"
    elif state.get("action_type") == "revise candidate's work experiences":
        # Placeholder for revising work experiences logic
        state["revised_work_experiences"] = "Revised work experiences"
    elif state.get("action_type") == "create candidate's cover letter":
        # Placeholder for creating cover letter logic
        state["ai_cover_letter"] = "AI generated cover letter"
    elif state.get("action_type") == "create candidate's message to hiring manager":
        # Placeholder for creating message to hiring manager logic
        state["ai_hiring_manager_message"] = "AI generated message to hiring manager"
    elif state.get("action_type") == "revise entire resume":
        # Placeholder for revising entire resume logic
        pass  # Implement the revision logic here

    return state

graph_builder = StateGraph(State)

graph_builder.add_node("action_classifier", classify_message)
graph_builder.add_edge(START, "action_classifier")
graph_builder.add_edge("action_classifier", END)

graph = graph_builder.compile()


def run_chatbot():
    # Initialize Chat History
    state = {"messages": []}

    user_prompt = st.text_area("Chat with REACT", key="user_prompt")
    # user_prompt = input("Enter your message:")
    
    if user_prompt:
        state["messages"] = state.get("messages", []) + [
            {"role": "user", "content": user_prompt}
        ]

        state = graph.invoke(state)

        if state.get("messages") and len(state["messages"]) > 0:

            print(f"Decision: {state.get("action_type")} with a confidence of {state.get("action_confidence")}")
            print(f"Scope: {state.get("scope_selection")} with a confidence of {state.get("scope_confidence")}")