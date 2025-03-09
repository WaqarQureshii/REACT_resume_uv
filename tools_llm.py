from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI

from tools_firebase import get_user_db

def get_resume_formatted_for_llm(collection_type: str) -> str:
    user_db = get_user_db()
    collections = user_db.collection(collection_type)

    result = []

    for doc in collections.stream():
        data=doc.to_dict()
        
        # Retrieve the job name and other fields
        job_title = data.get("role", "UNKNOWN ROLE")
        company = data.get("organization", "UNKNOWN ORGANIZATION")
        start_date = data.get("start_date", "YYYY-MM")
        if data.get("present"):
            end_date = "Present"
        else:
            end_date = data.get("end_date", "YYYY-MM")

        location = data.get("location", "UNKNOWN LOCATION")

        experiences = [
            value for key, value in data.items()
            if key.startswith("experience_description") and value
        ]

        result.append(f"Title: {job_title}\n")
        result.append(f"Company: {company}\n")
        result.append(f"Start Date: {start_date}\n")
        result.append(f"End Date: {end_date}\n")
        result.append(f"Location: {location}\n")
        for experience in experiences:
            result.append(f"- {experience}")

    return "\n".join(result)
                

job_experiences_system_prompt = '''
Extract key information from a job posting and use it to revise or generate strong, quantifiable bullet points for a person's job experience section in their resume.

When a person's job experience lacks details, generate viable situation-task-action-result bullet points based on the job description and typical responsibilities for the relevant job title. Please make it Applicant Tracking System-friendly.

# Steps

1. **Job Posting Analysis**: Extract all key skills, responsibilities, and qualifications relevant to the job from the given job description.
    - Please check again to see if you missed any points.
2. **Job Experience Review**: For each job experience provided (from most to least recent), analyze existing bullet points:
   - Identify the specific action taken.
   - Identify the scenario and context of the action.
   - Determine the quantifiable result as the outcome.
3. **Create Bullet Points*: Be prepared to create some from scratch if you don't have enough information from step 2. Using the Job Experience Review and Job Description Analysis create bullet points that:
   - Have depth by ensuring it has multiple key action verbs or skillsets that are related to the job description.
   - Explicitly state the actions taken by the person - be detailed in terms of mentioning who was involved, what skills it involved, the impact it had, the issue at hand etc.
   - Detail the quantifiable result using metrics or outcomes related to the job description - please use numeric values such as percentages of efficency gained/time saved/accuracy, $ impact of savings/budget/materiality. Don't limit yourself to those only.
   - Add context around the results and action.
   - Try to make them 2-3 lines-worth of content.
4. **Bullet Point Generation**: If a job experience contains minimal information:
   - Create viable action-result statements aligned with the key responsibilities and skills extracted from the job description.
   - Ensure these generated points are realistic for the given job title and industry.
   - Try to end up with 4-5 bullet points even if you have to generate some from scratch.
   - Have the creativity freedom to join two existing experiences into one if it creates consistent bullet point sizing without losing resume strength.
5. **Revising each bullet point**: Please check again to ensure that each bullet point meets Step 2's requirement while staying Applicant Tracking System friendly.
6. **Sort revised bullet points in the order of importance**: Sort the bullet points by what you deem to be critical based on the job description and what is deemed most important.

# Output Format

Provide key skillsets or experiences you deemed were important in step 1 before sending the revised bullet points over.

Provide a list of revised or new bullet points for each job experience. Bullet points should:
- Begin with a strong action verb.
- Include either multiple actions or skillsets involved.
- Try to make them 2-3 lines-worth of content.
- Add context to the situation to add depth to the bullet point.
- Include specific actions.
Include quantifiable outcomes such as percentage impact, dollar impact, headcount impact, number of rows automated, number of systems integrated etc
- Include specific actions that got the result.
- Be clear and concise.

# Examples

**Input Job Description**:
- Skills: Project management, team leadership managing multiple teams, budget oversight.
- Responsibilities: Coordinate cross-functional teams, manage project timelines, ensure resource allocation.

**Input Job Experience**:
- Title: Project Manager
- Company: XYZ Corp
- Dates: Jan 2020 - Present
- Existing Bullet: "Managed projects."

**Output**:
Key Skillsets from the job description:
Project Management skills, cross-functional leadership, managing budgets.

Here are the revised bullet points:
- Provide financial advisory services to business leaders across the organization while coordinating work portfolios among FP&A analysts. Connecting FP&A analysts with business leaders to prepare enterprise long-range planning models, quarterly and monthly internal reporting including variance analysis for executives, Translink reporting and other ad-hoc projects.
- Finance business partner to the Vice President of Engineering, partnering with 2 Senior Directors and 21 managers / staff to manage over $50 million through the development of actionable category level strategies, providing financial insight, market analysis and management of business plans - instrumental in reaching 97% forecast KPI metrics.

# Notes
- Ensure that each generated bullet point aligns with typical responsibilities for the given job role and industry.
- If possible, maintain a consistent style and format throughout the resume for professionalism.
'''

def get_openai_response(llm_selection: str, model_selection: str, job_description: str):
    messages = [
        SystemMessage(
            content=job_experiences_system_prompt
        ),
        AIMessage(
            content="Okay, please send over the job description first."
        ),
        HumanMessage(
            content=job_description
        ),
        AIMessage(
            content="Thank you, I will include the main skillsets and experiences I think are required for the job before my revised resume. I will do this after you send your job experiences."
        ),
        HumanMessage(
            content=get_resume_formatted_for_llm("experience")
        )
    ]   
    
    if llm_selection == "OpenAI":
        model = ChatOpenAI(model=model_selection, api_key=st.secrets.llm_keys.openai_key)
    elif llm_selection == "GoogleGemini":
        model = ChatGoogleGenerativeAI(model=model_selection, api_key=st.secrets.llm_keys.google_gemini_key)
    ai_message = model.invoke(messages)
    st.write(ai_message.content)
    