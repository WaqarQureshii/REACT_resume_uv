from langchain.prompts import ChatPromptTemplate, PromptTemplate

def job_analysis():
  template = '''
You are a resume optimization expert. Analyze the following job posting and extract:
1. Key themes and responsibilities
2. Core competencies required (skills, qualifications, certifications)
3. Keywords and phrases important for ATS
4. Tone and seniority of the role
5. Summary of top candidate profile fit

# Output in a string format as follows:
Themes: List them out,
Competencies: item1, item 2, item 3,
Key words/Phrases: keyword1, keyword2, key phrase3,
Tone And Seniority: text,
Ideal Candidate Summary: summary

Use the following information.
**Job Posting**: {job_posting}
  '''

  return PromptTemplate.from_template(template)



def candidate_analysis():
    
    template = '''
**Compare the candidate's experience and summary with the job posting analysis provided. Identify:**
- Strongest matches (skills, themes, industries, responsibilities)
- Gaps (missing qualifications, experience, terminology)
- Improvement Opportunities (in tone, keyword alignment, clarity)

# Output in a string format as follows:
Matches: List them out,
Gaps: List them out,
Improvements: List them out
  
Use the following informations.
1) **CANDIDATE EXPERIENCE LIST**: {candidate_experience_list}

2) **CANDIDATE PROFESSIONAL SUMMARY**: {candidate_professional_summary}

3) **Job Posting Analysis**: {job_posting_analysis}
'''
    return PromptTemplate.from_template(template)


def ai_work_experience(x):
   template = '''
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

  # Output in a string Format as follows:
  - Bullet Point 1
  - Bullet Point 2
  ...
  - Bullet Point 15

# Notes
  - Use a variety of results such as days, hours, number of systems, number of people/headcount.
  - Use common themes or langauge outlined in the job posting analysis.

# Use the following
  **Job Posting Analysis**: {job_posting_analysis}

  **Candidate Analysis**: {candidate_analysis}
  '''
   return PromptTemplate.from_template(template)




def ai_professional_summary(x):
   template = '''From the provided Job Posting Analysis, create 5 high-quality bullet points that would fit into a candidate's Professional Summary section.

# Steps
  1. Using the analysis provided about the job posting, write 5 bullet points for a candidate’s professional summary section. Make these highly tailored to the job posting and designed to attract the hiring manager.

# Notes
  - Use common themes or language outlined in the job posting analysis.

# Use the following
# **Job Posting Analysis**: {job_posting_analysis}
  '''
   return PromptTemplate.from_template(template)

def ai_career_taglines(x):
   template = '''**Generate 3 career taglines that are relevant to the job posting provided to you: Ensure they are descriptive of skills rather than a specific role or position.
  - Keep it related to technical skills, high-level accomplishments and soft skills.
  - Keep it to 2-3 words max for each tagline.
  - Output 3 taglines.
  
  # Output Format:
  Tagline 1, Tagline 2, Tagline 3

  # Use the following
  **Job Posting**: {job_posting}
  '''
   return PromptTemplate.from_template(template)


# Returns suggested content

def ai_summary_of_skills(x):
    template = '''
From the provided Job Posting, create 5 high-quality bullet points that would fit into a candidate's Summary of Skills section.

# Steps
  1. Using the analysis provided about the job posting, create 5 bullet points for a candidate’s summary of skills section. Make them specific to the job posting and aligned with the hiring manager’s priorities.

# Notes
  - Use common themes or language outlined in the job posting analysis.

# Use the following
**Job Posting**: {job_posting_analysis}
'''
    return PromptTemplate.from_template(template)


def revision_work_exp1():
   template = '''You are a resume optimization specialist. Improve the following Candidate's work experience entry by rewriting it using the suggestions and analysis provided. Retain any unique details or accomplishments from the original, but ensure that the final output:
   - *do not* repeat and avoid repetition from Your Revised Experiences.
   - Aligns with the job analysis and candidate analysis by covering off any gaps and/or uses strengths by utilizing some of Suggested Work Experience Bullet Points
   - Avoids repeating content
   - Contains 5-6 bullet points
   - Uses either a W,X,Y,Z format or Z,X,Y format where
    W = Specifics of the action Z below, EXAMPLE: "leveraging strong technical background in SQL and Generative AI tools"
    X = the result (try to fit in language from the job posting). FOR EXAMPLE: "Reduced errors",
    Y = the quantifiable impact. FOR EXAMPLE: "by 40%",
    Z = how it was accomplished (try to utilize the job posting analysis provided), FOR EXAMPLE: "after creating a new Standard Operating Procedure.":
    # Example of X,Y,Z,W: Reduced errors by 40% after creating a new Standard Operating Procedure leveraging strong technical background in SQL and Generative AI tools.
    # Example of Z,X,Y,W: Spearheaded Power BI Implementation enterprise wide that reduced time generating manual reports by 2 business days, involving 2 weeks of change management training.

    # Steps
    1) Create the bullet points using the guidance above
    2) Sort each bullet point from what you think is the most attractive to the Hiring Manager based on the job analysis provided to you to the least attractive.

    # Output Format:
    Candidate's Role @ Candidate's Company Workd At. City, Country. [Start Date] - [End Date or Present]. URL Link to Company:
    - Re-written Bullet Point
    - Re-written Bullet Point
    - Re-written Bullet Point
    - Re-written Bullet Point
    - Re-written Bullet Point


    --Candidate's Actual Work Experience to be completely re-written and overhauled:
    {work_exp_to_be_revised}

    --Job Analysis--
    {job_posting_analysis}

    --Candidate Match Analysis--
    {candidate_analysis}

    --Suggested Work Experience Bullet Points--
    {ai_work_exp}

    --Revised Working Experiences--
    {revised_work_exp}
   '''
   return PromptTemplate.from_template(template)


def revision_work_exp2():
  template = '''You are a world-class resume optimization specialist.

Your task is to **completely rewrite** the following Candidate's work experience entry using the suggestions and analysis provided. You may **discard, reframe, or significantly transform** the original content as needed. The final result should read like an optimized, keyword-rich, results-driven, ATS-friendly resume.

## Important Guidelines:
- *Avoid repetition* from Your Revised Experiences
- DO NOT treat the original experience as final—use it as optional input for context or detail.
- Your top priority is to **leverage the Suggested Bullet Points** and **align with the Job Analysis**.
- Retain **only unique, verifiable, or impressive accomplishments** from the original if they add measurable value.
- Be bold in rewriting: synthesize, combine, modernize, and clarify the content.
- Incorporate industry language, strategic tone, and metrics that reflect a high-performing candidate.
- Integrate the W,X,Y,Z or Z,X,Y,W structure:
  ### Examples:
  - **X,Y,Z,W**: Reduced errors by 40% after creating a new Standard Operating Procedure leveraging strong technical background in SQL and Generative AI tools.
  - **Z,X,Y,W**: Spearheaded enterprise-wide Power BI implementation that reduced report generation time by 2 business days, involving 2 weeks of change management training.

## Steps:
1) Based on the job analysis and candidate analysis, keep which ever bullet point from the original experience and optimize it by modifying it to align with the job posting.
2) If after step 1, you don't have 6 bullet points, then leverage the suggested bullet points to fill in the gaps and based on the original experience's job title to make it more contextually appropriate.
3) Ensure each bullet point is sorted from most relevant to the job analysis → to least relevant.

## Output Requirements:
- Exactly 5–6 bullet points
- Sorted from most relevant to the job analysis → to least
- Each bullet point must use quantifiable metrics or impact language
- Incorporate job-specific keywords from the analysis
- DO NOT repeat ideas across bullets

## Output Format:
**[Candidate's Role] @ [Company Name]. [City, Country]. [Start Date] – [End Date or Present]. [Company URL]**
- Bullet Point 1
- Bullet Point 2
- Bullet Point 3
- Bullet Point 4
- Bullet Point 5
- Bullet Point 6 (optional)

## Source Material:

### Original Experience (for context only – do NOT copy blindly):
{work_exp_to_be_revised}

### Job Analysis:
{job_posting_analysis}

### Candidate Analysis:
{candidate_analysis}

### Suggested Bullet Points:
{ai_work_exp}

###Your Revised Experiences
{revised_work_exp}

    '''
  return PromptTemplate.from_template(template)


def revision_professional_summary():
  template = '''You are a world-class resume optimization specialist.

Your task is to **completely rewrite** the following Candidate's Professional Summary entry using the suggestions and analysis provided. You may **discard, reframe, or significantly transform** the original content as needed. The final result should read like an optimized, keyword-rich, results-driven, ATS-friendly resume.

## Important Guidelines:
- DO NOT treat the original summary as final—use it as optional input for context or detail.
- Your top priority is to **leverage the Suggested Bullet Points** and **align with the Job Analysis**.
- Retain **only unique, verifiable, or impressive accomplishments** from the original if they add measurable value.
- Be bold in rewriting: synthesize, combine, modernize, and clarify the content.
- Incorporate industry language, strategic tone, and metrics that reflect a high-performing candidate.
- Ensure each bullet point highlights:
  a. A few key essential skills to the role. Example: Experienced Marketing Manager with 8+ years of expertise in driving innovative campaigns.
  b. Shows the value by adding in one or two significant achievements or contributions. Example: "Successfully increased sales revenue by 25% through targeted marketing efforts."
  c. And lastly mention professional qualities: add a personal trait that adds value to the expertise. Example: Dynamic and results-oriented team leader with excellent communication skills."

## Steps:
1) Based on the job analysis and candidate analysis, keep which ever bullet point from the original summary and optimize it by modifying it to align with the job posting.
2) If after step 1, you don't have 5 bullet points, then leverage the suggested bullet points to fill in the gaps and based on the job title to make it more contextually appropriate.
3) Ensure each bullet point is sorted from most relevant to the job analysis → to least relevant.

## Output Format:
- Highly tailored Professional Summary Bullet point 1
- Highly tailored Professional Summary Bullet point 2
- Highly tailored Professional Summary Bullet point 3
- Highly tailored Professional Summary Bullet point 4
- Highly tailored Professional Summary Bullet point 5

## Source Material:
### Original Professional Summary (for context only – do NOT copy blindly):
{candidate_professional_summary}

### Job Analysis:
{job_posting_analysis}

### Candidate Analysis:
{candidate_analysis}

### Suggested Bullet Points:
{ai_prof_summary}
'''
  return PromptTemplate.from_template(template)


def generate_cover_letter():
  template = '''Write up a very concise and to the point cover letter incorporating bullet points into the content to make it easy to read. Utilize work experience points and the professional summary points provided to you as well as the job analysis.
  **Notes**:
    - Incorporate and naturally pack appropriate skills used into the cover letter.
    - Incorporate my voice by adding my achievements and anecdotes that only I could have provided.
    
  ## Work Experience Points:
  {revised_work_exp}

  ## Professional Summary Points:
  {revised_prof_summary}

  ## Job Analysis:
  {job_posting_analysis}
    '''
  return PromptTemplate.from_template(template)


def generate_message_to_hiring_manager():
  template = '''Please generate a brief but compelling message to the hiring manager using your generated content and your analysis utilizing the cover letter provided to you:
  
  {cover_letter}'''
  return PromptTemplate.from_template(template)