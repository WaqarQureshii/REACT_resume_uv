chain_1_job_analysis = '''
Analyze the following job posting that I will provide to you. Identify all of the key skills, responsibilities, qualifications, and results/achievements the hiring manager is looking for. Extract specific action words, priorities, and themes used in the job description.

# Output format:
  Job Title and Team:

  Job Posting's Key Skills, Responsibilities and Results/Achievements:

  Job Posting Themes:
    - Action words commonly used:
    - Priorities mentioned:
    - General Theme of job posting:

  Job Posting Analysis Summary:

'''
# Returns Job Analysis

chain_2a_tailored_work_exp = '''
From the provided Job Posting Analysis, create high-quality bullet points that would fit into a candidate's Work Experience Section.

# Steps
  1. (For Candidate's Work Experience Section) Using the analysis provided about the job posting, deliberately write 15 bullet points that could be included in the best fitted candidate's experience section. Ensure they are highly tailored to the job posting and appeal to the hiring manager.
  2. (For Candidate's Work Experience Section) Use either a W,X,Y,Z format or Z,X,Y format where
    W = Specifics of the action Z below, such as "leveraging strong technical background in SQL and Generative AI tools"
    X = the result (try to fit in language from the job posting) such as "Reduced errors",
    Y = the quantifiable impact such as "by 40%",
    Z = how it was accomplished (try to utilize the job posting analysis provided), for example "after creating a new Standard Operating Procedure.":
    # Example of X,Y,Z,W: Reduced errors by 40% after creating a new Standard Operating Procedure leveraging strong technical background in SQL and Generative AI tools.
    # Example of Z,X,Y,W: Spearheaded Power BI Implementation enterprise wide that reduced time generating manual reports by 2 business days, involving 2 weeks of change management training.
  3. Sort them in ascending order in terms of the most captivating and aligned bullet point from the Hiring Manager's perspective.
  4. Within each bullet point, add appropriate amount of detail in terms of any context of the teams, systems, deadlines, or anything impressive to mention.
  5. Within each bullet point, be sure to include more specifics such as how these actions were completed. For example, which technical skills or soft skills were used

# Output Format
  - Bullet Point 1
  - Bullet Point 2
  ...
  - Bullet Point 15

# Notes
  - Use a variety of results such as days, hours, number of systems, number of people/headcount.
  - Use common themes or langauge outlined in the job posting analysis.
'''
# Returns suggested content

chain_2b_tailored_prof_summary = '''
From the provided Job Posting Analysis, create 5 high-quality bullet points that would fit into a candidate's Professional Summary section.

# Steps
  1. Using the analysis provided about the job posting, write 5 bullet points for a candidate’s professional summary section. Make these highly tailored to the job posting and designed to attract the hiring manager.

  # Notes
    - Use common themes or language outlined in the job posting analysis.
'''
# Returns suggested content

chain_2c_tailored_summaryofskills = '''
From the provided Job Posting Analysis, create 5 high-quality bullet points that would fit into a candidate's Summary of Skills section.

# Steps
  1. Using the analysis provided about the job posting, create 5 bullet points for a candidate’s summary of skills section. Make them specific to the job posting and aligned with the hiring manager’s priorities.

  # Notes
    - Use common themes or language outlined in the job posting analysis.
'''
# Returns suggested content

chain_2d_career_taglines = '''**Generate 3 career taglines that are relevant to the job posting utilizing the analysis provided to you: Ensure they are descriptive of skills rather than a specific role or position.
  - Keep it related to technical skills, high-level accomplishments and soft skills.
  - Keep it to 2-3 words max for each tagline.
  - Output 3 taglines.
  
  # Output Format:
  Tagline 1, Tagline 2, Tagline 3
  '''


chain_2e_candidate_analysis = '''
# Steps
  1. **Compare candidate with the job posting analysis provided**: Compare the candidate's provided experience list and professional summary provided later, against the job posting analysis that is also provided to you currently. Identify areas of alignment in strengths and skills, as well as gaps.
  
  2. **Provide Suggestions on Enhancements**: Using the identified alignment and gaps from the step before, suggest how the candidate’s experience could be rephrased or enhanced to better align with the job posting.
    - Include suggestions on the key words/phrases that can be used more.
    - Include suggestions on key bullet points that could be strengthened.


**CANDIDATE EXPERIENCE LIST**
{candidate_experience_list}

**CANDIDATE PROFESSIONAL SUMMARY**
{candidate_professional_summary}
'''

chain_3aa_work_experience = '''Please create a work experience section for the provided job the candidate held to you. You will do this by:
1) Understanding what the Hiring Manager is looking for by assessing the Job Analysis provided to you later.
2) Combine the "Highly Refined Bullet Points" that will be provided to you later and the "Candidate Analysis" that is provided to you.
As mentioned, you will be provided with the following after this as you ask for them:
  1) Candidate Analysis
  2) Job Analysis
  3) Candidate's working experience
  4) Highly Refined Bullet Points.'''

chain_3ab = '''Understand the Candidate Analysis provided to you and all of the relevant suggestions, strengths and weaknesses. Understand it in the context of the Job Posting Analysis provided to you to understand what the Hiring Manager is looking for.'''

chain_3ac_work_experience = '''I will now '''

chain_3ad_work_experience = '''Completely re-write and 6 bulletpoints for the candidate's work experience by completely re-writing the whole thing from scratch. Combine everything you have to do this such as combining the Candidate Analysis, Job Posting Analysis, Highly Refined Bullet Points and Candidate's Work Experience.
# Steps
  1) Once completed all the bullet points for each job, be sure to implement some of the key words and themes as well.
  2) Lastly, go through each bullet point once more to use either a W,X,Y,Z format or Z,X,Y format where
    W = Specifics of the action Z below, EXAMPLE: "leveraging strong technical background in SQL and Generative AI tools"
    X = the result (try to fit in language from the job posting). FOR EXAMPLE: "Reduced errors",
    Y = the quantifiable impact. FOR EXAMPLE: "by 40%",
    Z = how it was accomplished (try to utilize the job posting analysis provided), FOR EXAMPLE: "after creating a new Standard Operating Procedure.":
    # Example of X,Y,Z,W: Reduced errors by 40% after creating a new Standard Operating Procedure leveraging strong technical background in SQL and Generative AI tools.
    # Example of Z,X,Y,W: Spearheaded Power BI Implementation enterprise wide that reduced time generating manual reports by 2 business days, involving 2 weeks of change management training.
  4) After you have a new refined and aligned bullet point set for each job experience, sort the bullet points for each job from most attractive to the Hiring Manager to the least.

# Output Format:
  Candidate's Role @ Candidate's Company Workd At. City, Country. [Start Date] - [End Date or Present]. URL Link to Company:
  - Impactful Bullet Point
  - Impactful Bullet Point
  - Impactful Bullet Point
  - Impactful Bullet Point
  - Impactful Bullet Point'''
# Returns suggestions to make to existing experience


chain_3ba_professional_summary = '''Please create a revised professional summary section with the Highly Refined Bullet Points. Replace or combine any weaker points with the stronger, new ones while ensuring the final set aligns with the candidate analysis. End up with 5 bullet points.
You will be provided with the following after this as you ask for them:
  1) Candidate Analysis.
  2) The Candidate's current Professional Summary.
  3) Highly Refined Bullet Points.'''

chain_3bb_professional_summary = chain_3ab

chain_3bc_professional_summary = '''Read the Candidate's current professional summary in the context of the candidate analysis and note areas of improvement, gaps, points of alignments, or points that can be revamped or replaced.'''

chain_3bd_professional_summary = '''
# Steps
  1) Now go through all of the candidate's existing professional summary one-by-one, replace or combine as many weak points in the candidate's professional summary with the Highly Refined Bullet Points. Combine or replace bullet points that are less impactful with the highly refined ones and take into the consideration the candidate analysis, trying to implement as much as you can.
  2) Once completed all the bullet points, be sure to implement some of the key words and themes as well.
  3) After you have created and refined professional bullet points, go through each of the 5 bullet points to ensure each bullet point highlights:
    a. A few key essential skills to the role. Example: Experienced Marketing Manager with 8+ years of expertise in driving innovative campaigns.
    b. Shows the value by adding in one or two significant achievements or contributions. Example: "Successfully increased sales revenue by 25% throguh targeted marketing efforts."
    c. And lastly mention professional qualities: add a persona ltrait that adds value to the expertise. Example: Dynamic and results-oriented team leader with excellent communication skills."
  4) After you have a new refined and aligned bullet point set for each job experience, sort the bullet points for each job from most attractive to the Hiring Manager to the least.

  # Notes
  - Ensure each bullet emphasizes key skills, experiences, and results aligned with the job posting.
  - Begin with strong action verbs.
  - Address any if not all the candidate's weaknesses and showcase the candidate's strengths.

# Output Format:
  - Highly tailored Professional Summary Bullet point 1
  - Highly tailored Professional Summary Bullet point 2
  - Highly tailored Professional Summary Bullet point 3
  - Highly tailored Professional Summary Bullet point 4
  - Highly tailored Professional Summary Bullet point 5
  '''


chain_4a_generate_summary_of_skills ='''Your next task is to utilize the analysis to showcase the candidate's strengths and fill in the candidate's weaknesses by generating the Summary of Skills section of the candidate's resume.

# Steps
  1) Assess the Suggested Content within the Summary of Skills section of the **ANALYSIS**.
  2) use the Suggested Content and the User's existing experience to create 5 highly-tailored bullet points that summarizes the perfect candidate's technical skills, soft skills, or proven responsibilities for the job posting.
  3) Within each bullet point, ensure you formalize the appropriate amount of accountability in relation to the job title. For example, try to avoid implying "analyst-type" accountability for a "Director" role. Imply more "director-related" accountability.
  2) Describe the scenario they were used in with any accomplishments.
  3) Sort the points in descending order from most attractive to the Hiring Manager to the least.

  # Output Format:
  - Highly tailored Professional Summary Bullet point 1
  - Highly tailored Professional Summary Bullet point 2
  - Highly tailored Professional Summary Bullet point 3
  - Highly tailored Professional Summary Bullet point 4
  - Highly tailored Professional Summary Bullet point 5
'''

chain_4d_generate_career_taglines = '''**Generate 3 career taglines that are relevant to the job posting utilizing the analysis provided to you: Ensure they are descriptive of skills rather than a specific role or position.
  - Keep it related to technical skills, high-level accomplishments and soft skills required by the job.
  - Keep it to 2-3 words max for each tagline.
  - Output 3 taglines.
  
  # Output Format:
  Tagline 1, Tagline 2, Tagline 3
  '''

chain_5a_generate_cover_letter = '''Write up a very concise and to the point cover letter incorporating bullet points into the content to make it easy to read. Utilize work experience points and professionaly summary points provided to you as well as the job analysis..
  **Notes**:
    - Incorporate and naturally pack appropriate skills used into the cover letter.
    - Incorporate my voice by adding my achievements and anecdotes that only I could have provided.'''


chain_5b_generate_latex_resume = '''You will use a LaTeX template that will be provided later to edit with the candidate's information.:

# Steps:
  1) **Update the contact information and all their details using the below contact details from the candidate**: You will only replace the content and not any formatting and LaTeX structure unless you have to add or remove list items to fit the candidate's information.
  {contact_information}
  
  2) Update the 3 career taglines with the provided taglines **Candidate Information** provided to you at the end.
  
  3) Update the Professional Summary Section utilizing the section in the **Candidate Information** provided to you at the end.
  
  4) Update the Work Experience section utilizing the Work Experience section in the **Candidate's Information** provided to you at the end. Please input all of the job experiences and all 5 bullet points provided to you.:
  
  5) Update the Summary of Skills section using the Summary of Skills section in the **Candidate's Information** below.
  
  6) Update the Education Section with the Education Section below:
  {education_information}. Look for this information:
  
  7) Lastly, please appropriately escape with "\" before any % or & signs, as an example.
  
  # NOTE
   - You may have to create new list items or delete list items to make all of the candidate's information fit. Only use the LaTeX template as a guideline.
  
  **Candidate Analysis for Job Posting**:
  {analysis}

  **Candidate Resume Work Experience**:
  {work_experience}

  **Candidate Professional Summary**:
  {professional_summary}

  **Candidate Summary of Skills**:
  {summary_of_skills}

  **LaTeX Template**:
  {latex_template}

  # Output Format
  %% HEADER SECTION section LaTeX Code:
  (INSERT LATEX CODE)

  %% PROFESSIONAL SUMMARY section LaTeX code:
  (INSERT LATEX CODE for all 5 bullet points.)

  %% WORK EXPERIENCE section LaTeX code:
  (INSERT LATEX CODE to capture all the work experiences provided to you with all 5 bullet points for each experience.)

  %% EDUCATION section LaTeX code:
  (INSERT LATEX CODE)

  %% SUMMARY OF SKILLS section LaTeX code:
  (INSERT LATEX CODE for all 5 bullet points.)
  '''

_1_initial_prompt ='''
You are tasked with transforming a Candidate's resume based on a job posting to capture the Hiring Manager's attention and attract the Applicant Tracking System. Your goal is to create a highly tailored Experiences section within the resume and a Professional summary section that aligns with the job posting provided to you.

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
  5) Lastly, provide the individual jobs in chronological order based on the time the candidate worked there. I.e. the most recent job or present job would come first and oldest job is last.

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