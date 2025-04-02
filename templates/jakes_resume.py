jakes_resume = r'''
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

full_jakes_resume = r'''% FORMATTING START
\documentclass[letterpaper,12pt]{article}

\usepackage{latexsym}
\usepackage[empty]{fullpage}
\usepackage{titlesec}
\usepackage{marvosym}
\usepackage[usenames,dvipsnames]{color}
\usepackage{verbatim}
\usepackage{enumitem}
\usepackage[hidelinks]{hyperref}
\usepackage{fancyhdr}
\usepackage[english]{babel}
\usepackage{tabularx}
\input{glyphtounicode}
\usepackage{fontawesome}
\usepackage[top=0.4in, bottom=0.4in, left=0.4in, right=0.4in]{geometry}

\pagestyle{fancy}
\fancyhf{}
\fancyfoot{}
\renewcommand{\headrulewidth}{0pt}
\renewcommand{\footrulewidth}{0pt}


\urlstyle{same}

\raggedbottom
\raggedright
\setlength{\tabcolsep}{0in}

\titleformat{\section}{
  \vspace{-4pt}\scshape\raggedright\large
}{}{0em}{}[\color{black}\titlerule \vspace{-8pt}]

\pdfgentounicode=1

\newcommand{\resumeItem}[1]{
  \item\small{
    {#1 \vspace{-2pt}}
  }
}

\newcommand{\resumeSubheading}[4]{
  \vspace{4pt}\item
    \begin{tabular*}{0.97\textwidth}[t]{l@{\extracolsep{\fill}}r}
      \textbf{#1} & #2 \\
      \textit{\small#3} & \textit{\small #4} \\
    \end{tabular*}\vspace{-5pt}
}

\newcommand{\resumeSubSubheading}[2]{
    \item
    \begin{tabular*}{0.97\textwidth}{l@{\extracolsep{\fill}}r}
      \textit{\small#1} & \textit{\small #2} \\
    \end{tabular*}\vspace{-7pt}
}

\newcommand{\resumeProjectHeading}[2]{
    \item
    \begin{tabular*}{0.97\textwidth}{l@{\extracolsep{\fill}}r}
      \small#1 & #2 \\
    \end{tabular*}\vspace{-7pt}
}

\newcommand{\resumeSubItem}[1]{\resumeItem{#1}\vspace{-4pt}}

\renewcommand\labelitemii{$\vcenter{\hbox{\tiny$\bullet$}}$}

\newcommand{\resumeSubHeadingListStart}{\begin{itemize}[leftmargin=0.07in, label={}]}
\newcommand{\resumeSubHeadingListEnd}{\end{itemize}}
\newcommand{\resumeItemListStart}{\begin{itemize}}
\newcommand{\resumeItemListEnd}{\end{itemize}\vspace{-5pt}}

\begin{document}

% FORMATTING END

% RESUME START
%% HEADER SECTION
\begin{center}
    \textbf{\LARGE [Your Name, Your Designation]} \\
    \smallskip
    [Your Professional Tagline or Focus Area] \\
    \faLinkedinSquare \ \href{https://www.linkedin.com/in/username/}{linkedin.com/in/yourprofile} \quad \faEnvelope \ \href{mailto:your.email@example.com}{your.email@example.com} \quad \faPhone \ ([Your Phone Number])
\end{center}

%% PROFESSIONAL SUMMARY
\section{Professional Summary}
  \resumeItemListStart
    \resumeItem{Bullet Point about Professional Summary 1}
    \resumeItem{Bullet Point about Professional Summary 2}
    \resumeItem{Bullet Point about Professional Summary 3}
  \resumeItemListEnd

%% WORK EXPERIENCE
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

\section{Education}
  \resumeSubHeadingListStart
    \resumeSubheading
      {\href{https://www.college.com/degree}{[Degree, Field of Study]}}{[Graduation Year]}
      {[University Name]}{[Location]}
    \resumeSubheading
      {\href{https://www.college.com/degree}{[Certificate Name]}}{[Graduation Year]}
      {[University Name]}{[Location]}
  \resumeSubHeadingListEnd


\section{Summary of Skills}
  \resumeItemListStart
    \resumeItem{Bullet Point about Skills 1}
    \resumeItem{Bullet Point about Skills 2}
    \resumeItem{Bullet Point about Skills 3}
  \resumeItemListEnd

\end{document}
'''