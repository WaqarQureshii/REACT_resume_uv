from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnableLambda, RunnableParallel

from tools_firebase import get_firestore_collection, get_user_db
from prompts import prompts_1

def get_resume_formatted_for_llm(collection_type: str) -> str:
    Candidate_db = get_user_db()
    collections = Candidate_db.collection(collection_type)

    result = []

    for doc in collections.stream():
        data=doc.to_dict()
        
        if collection_type=="experience":
            # Retrieve the job name and other fields
            job_title = data.get("role", "UNKNOWN ROLE")
            company = data.get("organization", "UNKNOWN ORGANIZATION")
            start_date = data.get("start_date", "YYYY-MM")
            job_linkedin_url = data.get("linkedin_url", "None")
            if data.get("present"):
                end_date = "Present"
            else:
                end_date = data.get("end_date", "YYYY-MM")

            work_location = data.get("location", "UNKNOWN LOCATION")

            experiences = [
                value for key, value in data.items()
                if key.startswith("experience_description") and value
            ]

            result.append(f"Title: {job_title}\n")
            result.append(f"Company: {company}\n")
            result.append(f"LinkedIN URL: {job_linkedin_url}\n")
            result.append(f"Start Date: {start_date}\n")
            result.append(f"End Date: {end_date}\n")
            result.append(f"Location: {work_location}\n")
            for experience in experiences:
                result.append(f"- {experience}")

        if collection_type == "summary":
            skill = data.get("skill", "Unknown Skill")
            skill_summary = data.get("description", "Unknown description")

            result.append(f"Skill: {skill}")
            result.append(skill_summary)

        if collection_type == "education":
            institution = data.get("institution", "Unknown institution")
            degree = data.get("degree", "Unknown degree")
            education_url = data.get("website_url", "None")
            specialist = data.get("specialist", "Unknown")
            major = data.get("major", "Unknown")
            minor = data.get("minor", "Unknown")
            education_location = data.get("location", "Unknown")
            year_earned = data.get("year_earned", "Unknown")
            gpa = data.get("gpa", "Unknown")
            additional_info = data.get("additional_info", "Unknown")

            result.append(f"Institution: {institution}")
            result.append(f"Degree: {degree}, Specialist: {specialist}, Major: {major}, Minor: {minor}")
            result.append(f"Website URL: {education_url}\n")
            result.append(f"Location: {education_location}")
            result.append(f"Year Earned: {year_earned}")
            result.append(f"Additional Info: {additional_info}")

        if collection_type == "contact":
            email_address = data.get("email_address", None)
            first_name = data.get("first_name", None)
            last_name = data.get("last_name", None)
            contact_linkedin_url = data.get("linkedin_url", None)
            phone_number = data.get("phone_number", None)
            personal_website = data.get("personal_website", None)

            result.append(f"Email Address: {email_address}")
            result.append(f"Name: {first_name} {last_name}")
            result.append(f"LinkedIN URL: {contact_linkedin_url}")
            result.append(f"Phone Number: {phone_number}")
            result.append(f"personal_website: {personal_website}")


    return "\n".join(result)
                
latex_resume_header = r'''
\begin{center}
    \textbf{\LARGE [Your Name, Your Designation]} \\
    \smallskip
    [Your Professional Tagline or Focus Area] \\
    \faLinkedinSquare \ \href{https://www.linkedin.com/in/username/}{linkedin.com/in/yourprofile} \quad \faEnvelope \ \href{mailto:your.email@example.com}{your.email@example.com} \quad \faPhone \ ([Your Phone Number])
\end{center}'''

latex_working_experience = r'''
\section{Experience}
  \resumeSubHeadingListStart

    \resumeSubheading
      {[Job Title 1]}{[Start Date] -- [End Date or Present]}
      {\href{https://www.linkedin.com/company/companyname/}{[Company Name]}}{[Location]}
      \resumeItemListStart
        \resumeItem{Bullet Point about Job Title 1}
        \resumeItem{Bullet Point about Job Title 1}
        \resumeItem{Bullet Point about Job Title 1}
      \resumeItemListEnd

    \resumeSubheading
      {[Job Title 2]}{[Start Date] -- [End Date]}
      {\href{https://www.linkedin.com/company/companyname/}{[Company Name]}}{[Location]}
      \resumeItemListStart
        \resumeItem{Bullet Point about Job Title 2}
        \resumeItem{Bullet Point about Job Title 2}
        \resumeItem{Bullet Point about Job Title 2}
      \resumeItemListEnd

  \resumeSubHeadingListEnd
'''
latex_professional_summary =r'''
\section{Professional Summary}
  \resumeItemListStart
    \resumeItem{Bullet Point about Professional Summary 1}
    \resumeItem{Bullet Point about Professional Summary 2}
    \resumeItem{Bullet Point about Professional Summary 3}
  \resumeItemListEnd
'''

latex_education = r'''
\section{Education}
  \resumeSubHeadingListStart
    \resumeSubheading
      {\href{https://www.college.com/degree}{[Degree, Field of Study]}}{[Graduation Year]}
      {[University Name]}{[Location]}
    \resumeSubheading
      {\href{https://www.college.com/degree}{[Certificate Name]}}{[Graduation Year]}
      {[University Name]}{[Location]}
  \resumeSubHeadingListEnd
'''

latex_summary_skills = r'''
\section{Skills}
  \resumeItemListStart
    \resumeItem{Bullet Point about Skills 1}
    \resumeItem{Bullet Point about Skills 2}
    \resumeItem{Bullet Point about Skills 3}
  \resumeItemListEnd
'''
latex_jakes_resume = r'''
%% HEADER SECTION
\begin{center}
    \textbf{\LARGE [Your Name, Your Designation]} \\
    \smallskip
    [Your Professional Tagline or Focus Area] \\
    \faLinkedinSquare \ \href{https://www.linkedin.com/in/username/}{linkedin.com/in/yourprofile} \quad \faEnvelope \ \href{mailto:your.email@example.com}{your.email@example.com} \quad \faPhone \ ([Your Phone Number])
\end{center}

%% PROFESSIONAL SUMMARY SECTION
\section{Professional Summary}
  \resumeItemListStart
    \resumeItem{Bullet Point about Professional Summary 1}
    \resumeItem{Bullet Point about Professional Summary 2}
    \resumeItem{Bullet Point about Professional Summary 3}
  \resumeItemListEnd

%% WORK EXPERIENCE SECTION
\section{Experience}
  \resumeSubHeadingListStart

    \resumeSubheading
      {[Job Title 1]}{[Start Date] -- [End Date or Present]}
      {\href{https://www.linkedin.com/company/companyname/}{[Company Name]}}{[Location]}
      \resumeItemListStart
        \resumeItem{Bullet Point about Job Title 1}
        \resumeItem{Bullet Point about Job Title 1}
        \resumeItem{Bullet Point about Job Title 1}
      \resumeItemListEnd

    \resumeSubheading
      {[Job Title 2]}{[Start Date] -- [End Date]}
      {\href{https://www.linkedin.com/company/companyname/}{[Company Name]}}{[Location]}
      \resumeItemListStart
        \resumeItem{Bullet Point about Job Title 2}
        \resumeItem{Bullet Point about Job Title 2}
        \resumeItem{Bullet Point about Job Title 2}
      \resumeItemListEnd

  \resumeSubHeadingListEnd

%% EDUCATION SECTION
\section{Education}
  \resumeSubHeadingListStart
    \resumeSubheading
      {\href{https://www.college.com/degree}{[Degree, Field of Study]}}{[Graduation Year]}
      {[University Name]}{[Location]}
    \resumeSubheading
      {\href{https://www.college.com/degree}{[Certificate Name]}}{[Graduation Year]}
      {[University Name]}{[Location]}
  \resumeSubHeadingListEnd

%% SUMMARY OF SKILLS SECTION
\section{Summary of Skills}
  \resumeItemListStart
    \resumeItem{Bullet Point about Skills 1}
    \resumeItem{Bullet Point about Skills 2}
    \resumeItem{Bullet Point about Skills 3}
  \resumeItemListEnd
'''

latex_options ={
    "jakes_resume": latex_jakes_resume
}

_4_template_input = f'''You be a professional LaTeX editor by taking given LaTeX snippets of code and replacing the information in it with information I provide to you keeping the same format. Here is what you will be provided after:
  1. Candidate contact information and the appropriate LaTeX snippet.
  2. Candidate Professional Summary and the appropriate LaTeX snippet
  3. Candidate Work Experience and the appropriate LaTeX snippet
  4. Candidate Education and the appropriate LaTeX snippet
  5. Candidate Summary of Skills and the appropriate LaTeX snippet
  6. Generated Candidate Career Taglines and the appropriate LaTeX snippet

# Steps
  1. **Update the Contact header information**
    - Utilizing the contact information provided and any links, you will add in and replace all contact information with the Candidate's.
    - Update and/or add any links that were provided and find a way to add it in to the Candidate's resume in a professional way (perhaps in the name or label)
  2. **Update the Career Taglines at the top of the resume**
    - Update the Career Taglines with the ones provided. If none, suggest some based on the Candidate's work experience.
  3. **Update the Professional Summary section with the one provided**
    - Feel free to add/remove bullet points in the LaTeX resume to fit the professional summary in.
  4. **Update all experiences from most recent to oldest order**
    - Input all of the candidate's work organization's information such as Name, website hyperlink in the name, job title, period candidate worked there.
  5. **Update the Education section based on the information provided to you**
    - feel free to add or remove educations in the template to fit however many educations the Candidate has.
    - Include any relevant links provided to you.
  6. **Update the summary of skills section**
    - Try to keep the Summary of Skills section in the same format provided to you and input it into the template.

# Notes
  - Keep the formatting the same as the LaTeX template provided to you.
  - Only update the content including adding or removing nubmer of items in a list to fit the candidate's information.

# Output format
  **Header information**
  LaTeX Code

  **Career Taglines**
  LaTeX code with Career Taglines

  **Professional Summary**
  LaTeX code with Candidate's Professional Summary content instead of template provided

  **Experiences**
  LaTeX code with Candidate's Working Experience content instead of template provided

  **Education Section**
  LaTeX code with Candidate's Education content instead of template provided

  **Summary of Skills**
  LaTeX code with Candidate's Summary of SKills content instead of template provided

|'''

_5_template_review = '''You are a professional LaTeX editor, please revise the revised resume given in LaTeX for any errors and consistency in formatting and the number of desired pages.

# Steps to fit the resume content in the desired number of pages, trying it in this order.
1. **Modify the margins and/or spacing**: Try adjusting the numerical values of some of the margins and spacing within the pre-amble.
  - If this makes it fit, then please skill step 2 and move on to step 3.
2. **Editing or removing the oldest work experiences the candidate has on their resume**:
  - Look at editing and possibly removing the oldest work experiences on the Candidate's resume, perhaps making it more concise and/or removing some of those bullet points all all together.
  - Assess if it now fits the desired number of pages. If it doesn't, then repeat the process from Step 1.
3. **Review LaTeX code to ensure there are no errors**
  - check for consistency in formatting and that it is error-free.
  - Ensure there is a "\" before any "$" or "&".
4. **Do a final check on the output**:
  - Ensure there is a new line and properly inputted LaTeX code.
  - Ensure all characters are correctly escaped.
  - Ensure no part of the resume is accidentally commented out and not being activated.

'''

def get_llm_response(llm_selection: str, model_selection: str, messages: str):
    
    if llm_selection == "OpenAI":
        model = ChatOpenAI(model=model_selection, api_key=st.secrets.llm_keys.openai_key)
    elif llm_selection == "GoogleGemini":
        model = ChatGoogleGenerativeAI(model=model_selection, api_key=st.secrets.llm_keys.google_gemini_key, temperature=0.7)
    ai_message = model.invoke(messages)
    return ai_message.content


def get_revised_resume_chunks(llm_selection: str, model_selection: str, job_posting: str, latex_format: str, number_of_pages: int):
    stage_1_messages =[ 
        SystemMessage(content=prompts_1._1_initial_prompt),
        AIMessage(content="Understood, I will wait for your next steps."),
        SystemMessage(content=prompts_1._2_job_analysis),
        AIMessage(content="Please send over the job posting so I can analyze it as directed."),
        HumanMessage(f'''**Job Posting**:
                     
                     {job_posting}'''),
        AIMessage("I identified all of the key skills, responsibilities, qualifications, and results desired by the hiring manager. I identified specific action words, priorities and themes used. I will use this analysis to guide the rest of my work."),
        SystemMessage(content=prompts_1._3_analyze_experiences),
        AIMessage(content="Understood, please send the Candidate's work experience and professional summary."),
        HumanMessage(content=
                     f'''Here are the Candidate's Work experiences and professional summary:
                     
                    **Professional Summary**
                    {get_resume_formatted_for_llm("summary")}

                    **Work Experience**
                    {get_resume_formatted_for_llm("experience")}
                     '''),
        SystemMessage(content=prompts_1._4_generate_work_experiences),
        AIMessage(content="I have generated the experience content for the candidate. I will provide this at the end once we're completed all of the steps. Provide the next steps."),
        SystemMessage(content=prompts_1._5_generate_professional_summary),
        AIMessage(content="I have generated the Professional Summary content for the candidate. I will provide this and the Experience content previously generated once we're completed all of the steps. Provide then next steps."),
        SystemMessage(content=prompts_1._6_generate_summary_of_skills),
        AIMessage(content="I have generated the Summary of Skills content for the candidate. I will provide the Summary of Skills content, Experience content previously generated and the Professional Summary content previously generated once we're completed all of the steps. Provide then next steps."),
        SystemMessage(content=prompts_1._7_generate_career_taglines),
        AIMessage(content="I have generated 3 career taglines that will be sent all together with the other previous content generated."),
        SystemMessage(content=prompts_1._8_generate_message_to_hiring_manager),
        AIMessage(content="I have drafted uo a message to the hiring manager and will send this all together"),
        SystemMessage(content=prompts_1._9_output),
        AIMessage(content="Please see below the candidate's content generated from the previous steps.")
        ]
    
    _1_experience_response = get_llm_response(llm_selection, model_selection, stage_1_messages)
    with st.expander("Experience Response"):
        st.write(_1_experience_response)

    stage_2_messages =[
        SystemMessage(content=_4_template_input),
        AIMessage(content="Understood, I will wait for the individual pieces of information."),
        HumanMessage(
            content=
            f'''
            **Candidate's Professional Summary, Work Experience, Career Taglines, Summary of Skills**
            {_1_experience_response}

            **LaTeX Templates for Professional Summary**:
            {latex_professional_summary}

            **LaTeX Templates for Working Experience**:
            {latex_working_experience}

            **LaTeX Templates for Summary of Skills**:
            {latex_summary_skills}

            **Candidate's Contact Information**:
            {get_resume_formatted_for_llm("contact")}
            
            **LaTeX Templates for contact information and career taglines**:
            {latex_resume_header}

            **Candidate's Education information**:
            {get_resume_formatted_for_llm("education")}

            '''
        ),
        AIMessage(content="Below is your Revised LaTeX snippets with the candidate's information for all of the sections: Contact Information with career tagline, professional summary, working experience, summary of skills, education"),
        HumanMessage(content="Please input the revised LaTeX snippets into the following LaTeX template. I will provide the template in which you will be replacing the contents with in the next prompt."),
        AIMessage(content="Understood, please provide the LaTeX template that I will input the candidate's resume into."),
        HumanMessage(content=latex_jakes_resume),
        AIMessage(content="Please see the copy and pasteable LaTeX Template with the candidate's information instead.")
    ]

    final_response = get_llm_response("GoogleGemini", "gemini-2.0-flash", stage_2_messages)
    with st.expander("LaTeX Formatter response"):
      st.write(final_response)