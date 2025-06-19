import streamlit as st
from langchain_core.messages import AnyMessage, HumanMessage, ToolMessage, SystemMessage, AIMessage

from tools_general import login_user
from tools_firebase import get_firestore_value, get_user_information, get_resume_formatted_for_llm
from tools_langgraph import create_graph
from session_log import _get_session
import pprint


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
    

    st.button("Clear Chat", on_click=lambda: st.session_state.messages.clear())
    if 'graph' not in st.session_state:
        st.session_state.session_id = _get_session()
        st.session_state.messages =[]
        st.session_state.config = {"configurable": {"thread_id": str(_get_session())}}
        st.session_state.graph = create_graph(llm = llm_selection, llm_model=model_selection)

    chat_input_col1, chat_output_col2 = st.columns([3,1])
    if prompt := chat_input_col1.chat_input():
        st.session_state.messages.append({"role": "user", "content": prompt})  # Store messages as dict
        st.chat_message("human").write(prompt)
        
        response = st.session_state.graph.invoke({"messages": st.session_state.messages})  # Pass as dict
        final_response = None
        if 'messages' in response and isinstance(response['messages'], list) and response['messages']:
            msg = response['messages'][-1]
            if (hasattr(msg, 'content') and 
                msg.__class__.__name__ == 'AIMessage' and 
                msg.content and 
                msg.content.strip()):
                final_response = msg.content

        if final_response:
            st.chat_message("assistant").write(final_response)
            st.session_state.messages.append({"role": "assistant", "content": final_response})
        else:
            st.error("No valid response received")

    chat_output_col2.write(st.experimental_user.email)
