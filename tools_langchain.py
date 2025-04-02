import streamlit as st
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnableLambda, RunnableParallel

from tools_firebase import get_resume_formatted_for_llm
from prompts import prompts
from templates.jakes_resume import jakes_resume, full_jakes_resume

import time

def create_llm_model(llm_selection: str, model_selection: str):
    """Create the appropriate LLM model based on user selection.
    
    Args:
        llm_selection str: The LLM model of choice to complete the resume and job posting analysis.
            Google Gemini = GoogleGemini\n
            OpenAI = OpenAI\n
        model_selection str. The specific model of the LLM model.
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


def generate_prompt(prompt_text, ai_message):
    """Create a prompt template with the given system prompt and AI message."""
    return ChatPromptTemplate.from_messages([
        ("system", prompt_text),
        ("ai", ai_message)
    ])


class ResumeGenerator:
    def __init__(self, llm_selection, model_selection, job_posting):
        self.model = create_llm_model(llm_selection, model_selection)
        self.job_posting = job_posting
        self.input_dict = {}
        
        # Get resume sections
        self.contact_info = get_resume_formatted_for_llm("contact")
        self.education_info = get_resume_formatted_for_llm("education")
        self.professional_summary = get_resume_formatted_for_llm("summary")
        self.work_experience = get_resume_formatted_for_llm("experience")

        self.input_dict.update({
            "Candidate's Existing Working Experience": get_resume_formatted_for_llm("experience"),
            "Candidate's Existing Professional Summary": get_resume_formatted_for_llm("summary"),
            "Candidate's Contact Information": get_resume_formatted_for_llm("contact"),
            "Candidate's Education": get_resume_formatted_for_llm("education"),
            "Job Posting": job_posting
        })
    
        
    def generate_tailored_work_experience(self, analysis):
        prompt = ChatPromptTemplate.from_messages([
            ("system", prompts.chain_2a_tailored_work_exp)
        ])
        return prompt.format_prompt()
    
    def generate_tailored_prof_summary(self, analysis):
        prompt = ChatPromptTemplate.from_messages([
            ("system", prompts.chain_2b_tailored_prof_summary)
        ])
        return prompt.format_prompt()
    
    def generate_summaryofskills(self, analysis):
        prompt = ChatPromptTemplate.from_messages([
            ("system", prompts.chain_2c_tailored_summaryofskills)
        ])
        return prompt.format_prompt()
    
    def candidate_analysis(self, analysis):
        prompt = ChatPromptTemplate.from_messages([
            ("human", prompts.chain_2e_candidate_analysis),
            ("ai", "Understood, I understand the Job Analysis, now please provide the Candidate's Existing Working Experience as well as the Candidate's Existing Professional Summary. Start with the Working Experience"),
            ("human", self.input_dict["Candidate's Existing Working Experience"]),
            ("ai", "Perfect, now provide the Candidate's existing professional summary"),
            ("human", self.input_dict["Candidate's Existing Professional Summary"]),
            ("ai", "I have everything I need to complete the candidate analysis steps that you provided in the output format you outlined. Please see my response:")
        ])
        return prompt.format_prompt(candidate_experience_list=self.work_experience, candidate_professional_summary=self.professional_summary)
    
    def generate_career_tagline(self, analysis):
        prompt=ChatPromptTemplate.from_messages([
            ("human", prompts.chain_2d_career_taglines)
        ])
        return prompt.format_prompt()
    
    def _pause_execution(self, x):
        "Pause for one minute before proceeding."
        time.sleep(60)
        return x
    
    def run(self):
        """Run the complete resume generation pipeline and display results."""
        # Initial analysis chain
        job_analysis_prompt = ChatPromptTemplate.from_messages([
        ("human", prompts.chain_1_job_analysis),
        ("ai", "Understood. Please send over the job posting"),
        ("human", self.job_posting)
        ])

########### STAGE 1 ########
# ANALYSIS
        # job_analysis_model = create_llm_model("OpenAI", "o3-mini-2025-01-31")
        
        candidate_analysis_chain = RunnableLambda(self.candidate_analysis) | self.model | StrOutputParser() | RunnableLambda(self._pause_execution)
        work_exp_chain = RunnableLambda(self.generate_tailored_work_experience) | self.model | StrOutputParser() | RunnableLambda(self._pause_execution)
        prof_summary_chain = RunnableLambda(self.generate_tailored_prof_summary) | self.model | StrOutputParser() | RunnableLambda(self._pause_execution)
        summary_of_skills_chain = RunnableLambda(self.generate_summaryofskills) | self.model | StrOutputParser() | RunnableLambda(self._pause_execution)
        career_tagline_chain = RunnableLambda(self.generate_career_tagline) | self.model | StrOutputParser()

        all_sections = []
        analysis_chain = (
            job_analysis_prompt
            | self.model
            | StrOutputParser()
            | RunnableLambda(lambda x: self.input_dict.update({"Job Analysis": x}) or all_sections.append("Job Analysis") or x)
            | RunnableLambda(self._pause_execution)
            | RunnableParallel(branches={
                "Candidate Analysis": candidate_analysis_chain,
                "Suggested Work Experience": work_exp_chain,
                "Suggested Professional Summary": prof_summary_chain,
                "Suggested Summary of Skills": summary_of_skills_chain,
                "Suggested Career Taglines": career_tagline_chain,
                }
                )
        )
        analysis_result = analysis_chain.invoke({})


        for key in ["Suggested Work Experience", "Suggested Professional Summary", "Suggested Summary of Skills", "Suggested Career Taglines", "Candidate Analysis"]:
            all_sections.append(key)
            self.input_dict[key] = analysis_result["branches"][key]


########## STAGE 2 ###########
# Generating Final Resume Content
        # Initial generation chain
        
        generating_work_experience = ChatPromptTemplate.from_messages([
        ("human", prompts.chain_3aa_work_experience),
        ("ai", "Understood. Please send over the the Candidate Analysis, Candidate's Experience List and Highly Refined Bullet Points one-by-one as I tell you. Please send the Candidate Analysis first."),
        ("human", f"{prompts.chain_3ab}. **Candidate Analysis**: {self.input_dict["Candidate Analysis"]}"),
        ("ai", "Understood, I have a good understanding of the candidate's analysis that I will use a guide going forward. Send the Candidate's current job experiences."),
        ("human", f"{prompts.chain_3ac_work_experience}. **Candidate's Current Work Experience**: {self.input_dict["Candidate's Existing Working Experience"]}"),
        ("ai", "Based on the candidate analysis I have noted some weak bullet points that need to be replaced and some refinements that need to be made. Please send over the Highly Refined Bullet Points now."),
        ("human", f"Highly Refined Bullet Points: {self.input_dict["Suggested Work Experience"]}"),
        ("ai", "Perfect, I have everything I need to perform the next steps. Please provide the next steps."),
        ("human", prompts.chain_3ad_work_experience),
        ])

        work_experience_chain = (
            generating_work_experience
            | self.model
            | StrOutputParser()
            | RunnableLambda(lambda x: self.input_dict.update({"Revised Work Experience": x}) or all_sections.append("Revised Work Experience"))
        )
        work_experience_chain.invoke({})

        generating_prof_summary = ChatPromptTemplate.from_messages([
        ("human", prompts.chain_3ba_professional_summary),
        ("ai", "Understood. Please send over the the Candidate Analysis, Candidate's Professional Summary and Highly Refined Bullet Points one-by-one as I tell you. Please send the Candidate Analysis first."),
        ("human", f"{prompts.chain_3bb_professional_summary}. **Candidate Analysis**: {self.input_dict["Candidate Analysis"]}"),
        ("ai", "Understood, I have a good understanding of the candidate's analysis that I will use a guide going forward. Send the Candidate's current professional summary."),
        ("human", f"{prompts.chain_3bc_professional_summary}. **Candidate's Current Professional Summary**: {self.input_dict["Candidate's Existing Professional Summary"]}"),
        ("ai", "Based on the candidate analysis I have noted some weak bullet points that need to be replaced and some refinements that need to be made. Please send over the Highly Refined Bullet Points now."),
        ("human", f"Highly Refined Bullet Points: {self.input_dict["Suggested Professional Summary"]}"),
        ("ai", "Perfect, I have everything I need to perform the next steps. Please provide them."),
        ("human", prompts.chain_3bd_professional_summary),
        ])

        professional_summary_chain = (
            generating_prof_summary
            | self.model
            | StrOutputParser()
            | RunnableLambda(lambda x: self.input_dict.update({"Revised Professional Summary": x}) or all_sections.append("Revised Professional Summary"))
        )
        professional_summary_chain.invoke({})

        generating_summary_of_skills = ChatPromptTemplate.from_messages([
            ("system", prompts.chain_4a_generate_summary_of_skills),
            ("ai", "Understood, please see below.")
        ])
        summary_skills_chain = (
            generating_summary_of_skills
            | self.model
            | StrOutputParser()
            | RunnableLambda(lambda x: self.input_dict.update({"Revised Summary of Skills": x}) or all_sections.append("Revised Summary of Skills"))
        )
        summary_skills_chain.invoke({})

        generating_career_taglines = ChatPromptTemplate.from_messages([
            ("system", prompts.chain_4a_generate_summary_of_skills),
            ("ai", "Understood, please see below.")
        ])
        career_taglines_chain = (
            generating_career_taglines
            | self.model
            | StrOutputParser()
            | RunnableLambda(lambda x: self.input_dict.update({"Revised Career Taglines": x}) or all_sections.append("Revised Career Taglines"))
        )
        career_taglines_chain.invoke({})

        all_sections.extend(["Candidate's Existing Working Experience", "Candidate's Existing Professional Summary"])

        self._display_results(all_sections)


    def _display_results(self, section_list: list):
            # """Display the generated results in Streamlit expandable sections."""
            for section in section_list:
                with st.expander(section):
                    st.write(self.input_dict[section])

def run_chain(llm_selection: str, model_selection: str, job_posting: str):
    """Main function to run the resume generation pipeline."""
    generator = ResumeGenerator(llm_selection, model_selection, job_posting)
    generator.run()
