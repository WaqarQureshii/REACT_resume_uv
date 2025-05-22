import streamlit as st
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate, PromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnableLambda, RunnableParallel, RunnablePassthrough
from pprint import pprint

from tools_firebase import get_resume_formatted_for_llm
from tools_llm import get_resume_information_in_list
from prompts import prompts
from prompts.prompts import job_analysis, candidate_analysis, ai_work_experience, ai_professional_summary, ai_career_taglines, ai_summary_of_skills, revision_work_exp1, revision_work_exp2, revision_professional_summary, generate_cover_letter, generate_message_to_hiring_manager
from templates.jakes_resume import jakes_resume, full_jakes_resume

import time

def create_llm_model(llm_selection: str, model_selection: str):
    """Create the appropriate LLM model based on user selection.
    
    Args:
        llm_selection str: The LLM model of choice to complete the resume and job posting analysis.
            Google Gemini = GoogleGemini\n
            OpenAI = OpenAI\n
        model_selection str: The specific model of the LLM model.
            OpenAI o3-mini-2025-01-31 = o3-mini-2025-01-31\n
            OpenAI o1-mini-2024-09-12 = o1-mini-2024-09-12\n
            OpenAI gpt-4o-2024-08-06 = gpt-4o-2024-08-06\n
            Google Gemini gemini-1.5-pro = gemini-1.5-pro\n
            Google Gemini gemini-2.0-flash = gemini-2.0-flash\n
            Google Gemini gemini-2.0-flash-lite = gemini-2.0-flash-lite\n
        
    Returns: Union[ChatOpenAI, ChatGoogleGenerativeAI]: The initialized LLM model."""

    if llm_selection == "OpenAI":
        return ChatOpenAI(model=model_selection, api_key=st.secrets.llm_keys.openai_key)
    elif llm_selection == "GoogleGemini":
        return ChatGoogleGenerativeAI(
            model=model_selection, 
            api_key=st.secrets.llm_keys.google_gemini_key, 
            temperature=0.7
        )

class ResumeGenerator:
    def __init__(self, llm_selection, model_selection, job_posting):
        self.model = create_llm_model(llm_selection, model_selection)
        self.job_posting = job_posting
        self.input_dict = {}
        self.percent_complete = 0
        percent_complete = 0
        self.progress_bar = st.progress(percent_complete, text="Performing Job Posting analysis")
        self.revision_tab, self.analysis_tab, self.ai_content = st.tabs(["Revised Resume Sections", "Analysis", "AI Generated Content"])
        
        # Get resume sections
        self.contact_info = get_resume_formatted_for_llm("contact")
        self.education_info = get_resume_formatted_for_llm("education")
        self.professional_summary = get_resume_formatted_for_llm("summary")
        self.work_experience = get_resume_formatted_for_llm("experience")

        self.input_dict.update({
            "candidate_experience_list": get_resume_formatted_for_llm("experience"),
            "candidate_professional_summary": get_resume_formatted_for_llm("summary"),
            "Candidate's Contact Information": get_resume_formatted_for_llm("contact"),
            "Candidate's Education": get_resume_formatted_for_llm("education"),
            "job_posting": job_posting,
            "revised_work_exp": "",
            "work_exp_to_be_revised": "",
            "Cover Letter": None
        })
    
    def _pause_execution(self):
        "Pause for one minute before proceeding."
        time.sleep(60)

    def _assess_completion(self, increase:int, description: str):
        new_percent = self.percent_complete+increase
        self.progress_bar.progress(new_percent, description)

    def run(self):
        """Run the complete resume generation pipeline and display results."""
        all_sections = []

        # Stage 1: Job Posting and Candidate Analysis
        job_analysis_chain = (
            job_analysis()
            | self.model
            | StrOutputParser()
            | RunnableLambda(lambda x: self.input_dict.update({"job_posting_analysis": x}) or all_sections.append("job_posting_analysis")
            )
        )
        self._assess_completion(10, "Performing analysis on the candidate")
        job_analysis_chain.invoke(self.input_dict)


        candidate_analysis_chain = (
            candidate_analysis()
            | self.model
            | StrOutputParser()
            | RunnableLambda(lambda x: self.input_dict.update({"candidate_analysis": x}) or all_sections.append("candidate_analysis"))
        )
        candidate_analysis_chain.invoke(self.input_dict)
        self._assess_completion(15, "Generating highly tailored resume content based on a fictitious candidate.")
        candidate_analysis_chain.invoke(self.input_dict)
        self._pause_execution()

        # Stage 2: Generate Tailored Resume Content
        ai_chain = (
            RunnableParallel(branches={
                "Suggested Work Experience": RunnableLambda(ai_work_experience) | self.model | StrOutputParser() | RunnableLambda(lambda x: self.input_dict.update({"ai_work_exp": x}) or all_sections.append("ai_work_exp")),
                "Suggested Professional Summary": RunnableLambda(ai_professional_summary) | self.model | StrOutputParser() | RunnableLambda(lambda x: self.input_dict.update({"ai_prof_summary": x}) or all_sections.append("ai_prof_summary")),
                "Suggested Career Taglines": RunnableLambda(ai_career_taglines) | self.model | StrOutputParser() | RunnableLambda(lambda x: self.input_dict.update({"ai_career_taglines": x}) or all_sections.append("ai_career_taglines")),
                "Suggested Summary of Skills": RunnableLambda(ai_summary_of_skills) | self.model | StrOutputParser() | RunnableLambda(lambda x: self.input_dict.update({"ai_summary_of_skills": x}) or all_sections.append("ai_summary_of_skills")),
                }
            )
        )
        ai_chain.invoke(self.input_dict)
        self._assess_completion(25, "Revising candidate's work experience.")
        ai_chain.invoke(self.input_dict)
        self._pause_execution()


        # Stage 3: Revision of Work Experience
        experiences = get_resume_information_in_list("experience")
        for exp in experiences:
            job_title = exp.split("\n")[0].replace("Job Title: ", "").strip()
            company = exp.split("\n")[1].replace("Organization Name: ", "").strip()
            self._assess_completion(0, f"Working on {job_title} @ {company}")
            
            self.input_dict.update({"work_exp_to_be_revised": exp})

            work_revision_chain = (
                revision_work_exp2()
                | self.model
                | StrOutputParser()
                | RunnableLambda(lambda x: self.input_dict.update({"revised_work_exp": self.input_dict["revised_work_exp"] + x + "\n\n"}))
            )
            work_revision_chain.invoke(self.input_dict)

        all_sections.append("revised_work_exp")
        self._assess_completion(25, "Revising candidate's professional summary section")
        self._pause_execution()

        # Stage 4: Revision of Professional Summary
        prof_summary_revision_chain = (
            revision_professional_summary()
            | self.model
            | StrOutputParser()
            | RunnableLambda(lambda x: self.input_dict.update({"revised_prof_summary": x}) or all_sections.append("revised_prof_summary"))
        )
        prof_summary_revision_chain.invoke(self.input_dict)
        self._assess_completion(15, "Generating Cover Letter based on candidate's resume content and job posting analysis")

        # Stage 5: Generate Messaging
        cover_letter_chain = (
            generate_cover_letter()
            | self.model
            | StrOutputParser()
            | RunnableLambda(lambda x: self.input_dict.update({"cover_letter": x}) or all_sections.append("cover_letter"))
        )
        cover_letter_chain.invoke(self.input_dict)
        self._assess_completion(10, "Generating Hiring Manager message")

        hiring_manager_chain = (
            generate_message_to_hiring_manager()
            | self.model
            | StrOutputParser()
            | RunnableLambda(lambda x: self.input_dict.update({"hiring_manager_message": x}) or all_sections.append("hiring_manager_message"))
        )
        hiring_manager_chain.invoke(self.input_dict)        

        self._assess_completion(-self.percent_complete, "Complete")
        self._display_results(all_sections)

    def _display_results(self, section_list: list):
            # """Display the generated results in Streamlit expandable sections."""
            for section in section_list:
                if section == "ai_prof_summary":
                    with self.ai_content:
                        with st.expander("AI Professional Summary"):
                            st.write(self.input_dict[section])
                elif section == "ai_work_exp":
                    with self.ai_content:
                        with st.expander("AI Work Experience"):
                            st.write(self.input_dict[section])
                elif section == "ai_career_taglines":
                    with self.ai_content:
                        with st.expander("AI Career Taglines"):
                            st.write(self.input_dict[section])
                elif section == "ai_summary_of_skills":
                    with self.ai_content:
                        with st.expander("AI Summary of Skills"):
                            st.write(self.input_dict[section])
                elif section == "job_posting_analysis":
                    with self.analysis_tab:
                        with st.expander("Job Posting Analysis"):
                            st.write(self.input_dict[section])
                elif section == "candidate_analysis":
                    with self.analysis_tab:
                        with st.expander("Candidate Analysis"):
                            st.write(self.input_dict[section])
                elif section =="revised_prof_summary":
                    with self.revision_tab:
                        with st.expander("Revised Professional Summary"):
                            st.write(self.input_dict[section])
                elif section =="revised_work_exp":
                    with self.revision_tab:
                        with st.expander("Revised Work Experience"):
                            st.write(self.input_dict[section])
                elif section == "candidate_experience_list":
                    with self.revision_tab:
                        with st.expander("Current Experience"):
                            st.write(self.input_dict["candidate_experience_list"])
                elif section == "cover_letter":
                    with self.revision_tab:
                        with st.expander("Cover Letter"):
                            st.write(self.input_dict["cover_letter"])
                elif section == "hiring_manager_message":
                    with self.revision_tab:
                        with st.expander("Message to Hiring Manager"):
                            st.write(self.input_dict["hiring_manager_message"])
                else:
                    next

def run_chain(llm_selection: str, model_selection: str, job_posting: str):
    """Main function to run the resume generation pipeline."""
    print("NEW RUN")
    print("")
    generator = ResumeGenerator(llm_selection, model_selection, job_posting)
    generator.run()
