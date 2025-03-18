template = r'''
%%% Only edit font sizes, margin or space sizes! %%%

%%%----------- FORMATTING SECTION STARTED------------%%%
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

\pagestyle{fancy}
\fancyhf{}
\fancyfoot{}
\renewcommand{\headrulewidth}{0pt}
\renewcommand{\footrulewidth}{0pt}

\addtolength{\oddsidemargin}{-0.6in}
\addtolength{\evensidemargin}{-0.6in}
\addtolength{\textwidth}{1in}
\addtolength{\topmargin}{-.6in}
\addtolength{\textheight}{0.2in}
\addtolength{\textheight}{-0.01in}

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

%%%----------- FORMATTING SECTION ENDED------------%%%

\begin{document}

% RESUME START
% Header
\begin{center}
    \textbf{\LARGE Waqar Qureshi, CPA} \\
    \smallskip
    People Leader | Data-Driven Collaborator \\
    \faLinkedinSquare \ \href{https://www.linkedin.com/in/joeb/}{linkedin.com/in/joeb} \quad \faEnvelope \ \href{joebiden@gmail.com/}{joebiden@gmail.com} \quad \faPhone \ (123) 456-7890
\end{center}

\section{Professional Summary}
  \resumeItemListStart
    \resumeItem{Over 10 years of experienced Financial Process Automation leader with expertise in transforming financial systems to address bottlenecks, optimize efficiency, and enhance data integrity.}
    \resumeItem{Proven track record in deploying advanced technologies such as Python, Power BI, and Power Apps to drastically reduce manual efforts and support strategic decision-making.}
    \resumeItem{Skilled in collaborating with cross-functional teams to design and implement scalable automated solutions, enhancing operational efficiency and data-driven insights.}
    \resumeItem{Deep understanding of the energy sector, particularly in implementing technical solutions that align with Enbridge’s objectives of sustainability and operational excellence.}
    \resumeItem{Demonstrated success in driving process improvements within financial systems against aggressive timelines, leading to significant cost savings and productivity gains.}
  \resumeItemListEnd

\section{Experience}
  \resumeSubHeadingListStart

    \resumeSubheading
      {Manager, Finance Transformation}{2023 -- Present}
      {Trez Capital}{Vancouver, Canada}
      \resumeItemListStart
        \resumeItem{Lead development of high-performing team, improving data accountability by 30\% and report accuracy vital for decision-making.}
        \resumeItem{Transformed loan portfolio of \$5.4bn into actionable intelligence using SQL and Python, savings of 2.5 FTE monthly.}
        \resumeItem{Engage C-suite stakeholders with data-driven analyses to secure strategic alignment and adhere to performance benchmarks.}
        \resumeItem{Optimized data consolidation through Power BI, increasing availability of financial insights by 40\% for executive committees.}
      \resumeItemListEnd

    \resumeSubheading
      {Manager, Financial Planning \& Analysis}{2020 -- 2023}
      {TransLink/CMBC}{Vancouver, Canada}
      \resumeItemListStart
        \resumeItem{Reduced reporting errors by 20\% by implementing innovative Power BI solutions aligned with corporate strategies.}
        \resumeItem{Improved operational efficiency by 10\% through advanced financial modeling, aiding proactive decision-making.}
        \resumeItem{Optimized \$850M+ budget management, achieving a 5\% cost reduction through strategic oversight.}
        \resumeItem{Integrated Power BI for continuous improvement, elevating processes within a government framework.}
      \resumeItemListEnd

    \resumeSubheading
      {Senior Finance Business Partner}{2018 -- 2020}
      {Enbridge Inc}{Toronto, Canada}
      \resumeItemListStart
        \resumeItem{Boosted variance analysis post-system amalgamation, enhancing decision capabilities across finance and business units.}
        \resumeItem{Ensured 97\% forecast accuracy managing \$50M+ engineering budgets, aligning strategies with operational goals.}
        \resumeItem{Secured \$1M annually in budget reductions via collaborative strategic execution and data analysis.}
      \resumeItemListEnd

    \resumeSubheading
      {Financial Analyst}{2016 -- 2018}
      {Toronto Hydro Corporation}{Toronto, Canada}
      \resumeItemListStart
        \resumeItem{Led development of a forecasting model identifying over \$2M in savings, enhancing predictive financial capabilities.}
        \resumeItem{Modernized portfolio management to enhance data integrity for financial reporting on a \$35M average portfolio.}
      \resumeItemListEnd

    \resumeSubheading
      {Consultant / Financial Analyst}{2014 -- 2016}
      {Deloitte}{Toronto, Canada}
      \resumeItemListStart
        \resumeItem{Crafted pivotal P\&L models for risk assessment, recognized for impactful strategic integration by senior leadership.}
        \resumeItem{Directed \$100M financial planning for HR and IT, enabling effective annual budgeting and strategic processes.}
        \resumeItem{Contributed to accurate financial analyses, ensuring precision and reliability in reporting and compliance.}
      \resumeItemListEnd

  \resumeSubHeadingListEnd

\section{Education}
  \resumeSubHeadingListStart
    \resumeSubheading
      {University of Toronto}{Toronto, Canada}
      {Bachelor of Commerce in Accounting, Minor in Economics}{}
    \resumeSubheading
      {CPA Canada}{Toronto, Canada}
      {Professional Designation}{}
  \resumeSubHeadingListEnd

\section{Summary of Skills}
 \resumeItemListStart
        \resumeItem{Expertise in Python, SQL, Power BI, UiPath RPA technologies to streamline and automate financial operations.}
        \resumeItem{Exceptional problem-solving and analytical capabilities with demonstrated success in finance applications management.}
        \resumeItem{Strong leadership with experience in leading teams of finance professionals towards operational and strategic goals.}
        \resumeItem{Proven ability to translate complex business requirements into technical specifications for automation solutions.}
        \resumeItem{History of collaboration with cross-functional teams to drive major financial and operational improvements.}
      \resumeItemListEnd

\end{document}
'''

