from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from tools_firebase import get_user_db, get_resume_formatted_for_llm

_1_initial_prompt ='''
You are trasked with transforming a Candidate's resume based on a job posting to capture the Hiring Manager's attention and attract the Applicant Tracking System. Your goal is to create a highly tailored Experiences section within the resume and a Professional summary section that aligns with the job posting provided to you.

You will be provided with:
1) Job Posting: the job the Candidate is interested in applying to.
2) Candidate's Professional Summary
3) Candidate's Job Experiences at each job.

Follow the next steps carefully that I will be providing to you in order to capture the Hiring Manager's attention.
'''

_2_job_analysis = f'''
Start by analyzing the given job posting to identify all of the key skills, responsibilities, qualifications, and results desired by the hiring manager. Extract specific action words, priorities and themes.

Please also create bullet points that would best fit this role, this company and this industry in terms of a Professional Summary and some work experiences.

You will use this analysis and generated points to guide the rest of your work.

**Job Posting** being sent over.
'''

_3_analyze_experiences = '''You will be provided with:
1) Candidate's existing Professional Summary and
2) Candidate's existing Work Experiences at each job.

Your job right now is to analyze the candidate's current skills and experiences in relation to your job analysis and job posting:

  # Steps
  1) Using the insights from the job posting, analyze the strengths of the Candidate's experiences in terms of skills, experiences, or results that align with the job posting. You will use these later to generate the candidate's resume content.
  2) identify any gaps in terms of skills, work experiences, or results that the Candidate does not have from the Job Posting. You will use these gaps later to fill in the gap when extrapolating or creating resume content from scratch.
  3) Keep these strengths and weaknesses analysis in mind when generating resume content for the candidate.'''

_4_generate_work_experiences = '''Your next task is to utilize your analysis to showcase the candidate's strengths and fill in the candidate's weaknesses by generating the Experiences section of the candidate's resume:

# Steps
  1) Create 5 highly-tailored bullet points for each work experience the candidate provides to attract the Hiring Manager's attention. Each bullet point will start with strong action words, quantifying the results, and explaining specifically what those results translated to. You will do this by using a mixture of:
    a) The candidate's strengths that you've analyzed
    b) Adding in material that addresses the candidate's weaknesses in terms of skillsets, experiences, responsibilities etc.
    c) Formalizing the appropriate amount of accountability in relation to the job title in each of the bullet points.
  2) Ensure specific actions taken by the candidate are used, going into brief detail on the various impacts (teams, systems, processes, budgets etc.)
  3) Ensure specific results are quantified as a result of the actions ($ impact, Time impact, budget impact, number of steps impact, team impact, spend impact)
  4) Sort the points from descending order in terms of what points would most attract the Hiring Manager

# Notes
  - You are to use a mixture of the candidate's existing information and a mix of newly generated information
  - Ensure each bullet emphasizes key skills, experiences, and results aligned with the job posting.
  - Begin with strong action verbs.
  - Include multiple action words or skillsets involved to ensure alignment with the Job Posting.
  - Address any if not all the candidate's weaknesses and showcase the candidate's strengths.
  - Use similar language to the Job Posting, if possible.

# Output Format:
  Role @ Company Name. City, Country. [Start Date] - [End Date or Present]. URL Link to Company:
  - Highly tailored Bullet point 1
  - Highly tailored Bullet point 2
  - Highly tailored Bullet point 3
  - Highly tailored Bullet point 4
  - Highly tailored Bullet point 5

  Role @ Company Name. City, Country. [Start Date] - [End Date or Present]. URL Link to Company:
  - Highly tailored Bullet point 1
  - Highly tailored Bullet point 2
  - Highly tailored Bullet point 3
  - Highly tailored Bullet point 4
  - Highly tailored Bullet point 5
  '''

_5_generate_professional_summary ='''Your next task is to utilize your analysis to showcase the candidate's strengths and fill in the candidate's weaknesses by generating the Professional Summary section of the candidate's resume

# Steps
  1) Create 5 highly-tailored bullet points that summarizes key work experience or skillsets the job posting is looking for based on your analysis. You will do this using a mixture of:
    a) The candidate's strengths that you've analyzed
    b) Adding in material that addresses the candidate's weaknesses in terms of skillsets, experiences, responsibilities etc.
    c) Formalizing the appropriate amount of accountability in relation to the job title in each of the bullet points.
  2) Ensure each bullet point emphasizes key skills, experiences, responsibilities and results are aligned with the job posting)
  3) Sort the points from descending order in terms of what points would most attract the Hiring Manager

# Notes
  - You are to use a mixture of the candidate's existing information and a mix of newly generated information
  - Ensure each bullet emphasizes key skills, experiences, and results aligned with the job posting.
  - Begin with strong action verbs.
  - Address any if not all the candidate's weaknesses and showcase the candidate's strengths.
  - Use similar language to the Job Posting, if possible.

# Output Format:
  - Highly tailored Professional Summary Bullet point 1
  - Highly tailored Professional Summary Bullet point 2
  - Highly tailored Professional Summary Bullet point 3
  - Highly tailored Professional Summary Bullet point 4
  - Highly tailored Professional Summary Bullet point 5
'''

_6_generate_summary_of_skills ='''Your next task si to utilize your analysis to showcase the candidate's strengths and fill in the candidate's weaknesses by generating the Summary of Skills section of the candidate's resume

# Steps
  1) Create 5 highly-tailored bullet points summarizes the candidate's proven technical skills, soft skills, or proven responsibilities the job posting is looking for based on your analysis. You will do this using a mixture of:
    a) The candidate's strengths that you've analyzed
    b) Adding in material that addresses the candidate's weaknesses in terms of skillsets, experiences, responsibilities etc.
    c) Formalizing the appropriate amount of accountability in relation to the job title in each of the bullet points.
  2) Describe the scenario they were used in with any accomplishments.
  3) Sort the points from descending order in terms of what points would most attract the Hiring Manager
'''

_7_generate_career_taglines ='''Generate 3 career taglines that are relevant to the job posting**: Ensure they are descriptive of skills rather than a specific role or position. Keep it related to technical skills, high-level accomplishments and soft skills.
    - Keep it to 2-3 words max for each tagline.'''

_8_generate_message_to_hiring_manager = '''Please generate a brief but compelling message to the hiring manager using your generated content and your analysis.'''

_9_output = '''Please send all of the content that has been generated

# Output Format
**PROFESSIONAL SUMMARY**

**WORK EXPERIENCE**

**SUMMARY OF SKILLS**

**CAREER TAGLINES**

**MESSAGE TO HIRING MANAGER**

**Candidate's Strengths and Weaknesses**

**Overview of changes made**
'''