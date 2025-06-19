from pydantic import BaseModel, Field

from typing import Optional, Union

class ContactInformation(BaseModel):
    first_name: Optional[str] = Field(None, description="First name of the user")
    last_name: Optional[str] = Field(None, description="Last name of the user")
    email: Optional[str] = Field(None, description="Email address of the user")
    contact_linkedin_url: Optional[str] = Field(None, description="LinkedIn URL of the user")
    phone_number: Optional[str] = Field(None, description="Phone number of the user")
    personal_website: Optional[str] = Field(None, description="Personal website of the user. Optional field")
    country: Optional[str] = Field(None, description="Country location of the user. Optional field.")
    state_province: Optional[str] = Field(None, description="State or province location of the user. Optional field.")
    city: Optional[str] = Field(None, description="City location of the user. Optional field.")


class ProfessionalSummary(BaseModel):
    skill_and_summary: Optional[list[str]] = Field(None, description="Skill/Achievement: A brief summary of the user's professional background and skills. Should be concise and relevant to the job position being applied for")


class WorkExperience(BaseModel):
    organization_name: Optional[str] = Field(None, description="Name of the organization where the job was held")
    linked_in_url: Optional[str] = Field(None, description="LinkedIn URL of the organization. Optional field")
    job_location: Optional[str] = Field(None, description="Location of the job position")
    job_title: Optional[str] = Field(None, description="Title of the job position")
    start_date: Optional[str] = Field(None, description="Start date of of the job position. Format: YYYY-MMM. Example: 2024-Apr")
    end_date: Optional[str] = Field(None, description="End date of the job position. Format: YYYY-MMM. Example: 2024-Apr. Or None if currently employed")
    present_role : Optional[bool] = Field(None, description="True if the job is currently held, False otherwise. If True, end_date should be None")
    responsibilities: Optional[list[str]] = Field(None, description="List of skills, responsibilities and achievements in the job position. Each responsibility should be a string")


class Education(BaseModel):
    degree_or_diploma_name: Optional[str] = Field(None, description="Name of the degree, diploma or certificate earned. Example: Bachelor of Science")
    institution_name: Optional[str] = Field(None, description="Name of the institution where the degree was earned. Example: University of XYZ")
    year_earned: Optional[Union[int,str]] = Field(None, description="Year when the degree was earned. Format: YYYY. Example: 2024")
    location: Optional[str] = Field(None, description="Location of the institution. Optional field. Example: City, Country")
    specialization: Optional[str] = Field(None, description="Specialization or major of the degree. Optional field. Example: Computer Science")
    major: Optional[str] = Field(None, description="Major of the degree. Optional field. Example: Computer Science")
    minor: Optional[str] = Field(None, description="Minor of the degree. Optional field. Example: Mathematics")
    additional_info: Optional[str] = Field(None, description="Any additional information about the degree. Optional field. Example: Graduated with honors, GPA 3.8/4.0")


class Job_Analysis(BaseModel):
    key_themes_and_responsibilities: Optional[list[str]] = Field(None, description="List of key themes and responsibilities extracted from the job description. Each theme or responsibility should be a string")
    core_competencies_required: Optional[list[str]] = Field(None, description="List of core competencies required for the job position. Each competency should be a string")
    core_qualifications_required: Optional[list[str]] = Field(None, description="List of core qualifications required for the job position. Each qualification should be a string")
    keywords_and_phrases: Optional[list[str]] = Field(None, description="List of keywords and phrases extracted from the job description to make the resume ATS-friendly. Each keyword or phrase should be a string")
    tone_and_seniority_level: Optional[str] = Field(None, description="Tone and seniority of the role. Example: 'Professional tone, mid-level seniority'. This should be a concise description of the tone and seniority level of the job position")
    ideal_candidate_summary: Optional[str] = Field(None, description="Summary of the ideal candidate for the job position. This should be a concise description of the ideal candidate's skills, experience and qualifications")


class Candidate_Analysis(BaseModel):
    candidate_strengths: Optional[list[str]] = Field(None, description="Identified strengths of the candidate in term sof theri skills, themes, industries, responsibilities and qualifications in relation to the job description. Each strength should be a string")
    candidate_gaps: Optional[list[str]] = Field(None, description="Identified gaps of the candidate in terms of their skills, themes, industries, responsibilities and qualifications in relation to the job description. Each gap should be a string")
    improvement_opportunities: Optional[list[str]] = Field(None, description="Identified opportunities for improvement in the candidate's resume in term sof tone, keyword alignment, clarity and themes to better match the job description. Each opportunity should be a string")


class ResumeState(BaseModel):
    query: Optional[str] = Field(None, description="Query to be processed by the workflow. This should be a concise description of the user's request for resume building")
    contact_information: Optional[ContactInformation] = Field(None, description="Contact information of the user. Contains keys: first_name, last_name, contact_linkedin_url, phone_number, personal_website")
    user_professional_summary: Optional[list[ProfessionalSummary]] = Field(None, description="Professional summary of the user. Contains a brief summary, list of skills, and educational qualifications")
    user_work_experience: Optional[list[WorkExperience]] = Field(None, description="List of all of the user's work experiences. Each experience is a dictionary with keys: organization_name, linked_in_url, job_location, job_title, start_date, end_date, present_role")
    user_education: Optional[list[Education]] = Field(None, description="List of educational qualifications where each qualification is a dictionary with keys: degree_or_diploma_name, institution_name, year_earned, location, specialization, major, minor, additional_info")

    revised_professional_summary: Optional[list[ProfessionalSummary]] = Field(None, description = "List of professional summaries where the summary is highly detailed and formatted to the job description. The length of each should be a bullet point's length.")
    revised_work_experience: Optional[list[WorkExperience]] = Field(None, description="List of work experiences where the roles and responsibilities is highly detailed and formatted to the job description. The length of each role and responsibility should be a an appropriate bullet point in a resume.")
    education: Optional[list[Education]] = Field(None, description = "List of educational qualifications of the candidate.")
    
    job_description: Optional[str] = Field(None, description="Job description for the position being applied for. This should be a detailed description of the job requirements and responsibilities")
    job_description_analysis: Optional[Job_Analysis] = Field(None, description="Analysis of the job description. Contains keys: key_themes_and_responsibilities, core_competencies_required, core_qualifications_required, keywords_and_phrases, tone_and_seniority_level, ideal_candidate_summary")
    candidate_analysis: Optional[Candidate_Analysis] = Field(None, description="Analysis of the candidate's resume in relation to the job description. Contains keys: candidate_strengths, candidate_gaps, improvement_opportunities")
    cover_letter: Optional[str] = Field(None, description="Cover letter that is tailored to the job description highlighting the user's strengths and weaknesses in relation to the job description without showing unproven technical skills such as software or industry/company experience.")
    message_to_hiring_manager: Optional[str] = Field(None, description="Message to the hiring manager highlighting the candidate's key strenghts and alignments in relation to the job description without lying about the candidate's technical skills, softwares used or industry/company experience.")
