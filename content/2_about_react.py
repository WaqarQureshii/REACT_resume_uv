import streamlit as st
import time

st.title("About REACT")
st.subheader("What Does REACT Do Differently?")

about_copy = """
Most resume builders help you format your resume—REACT goes beyond that. It :blue[**intelligently refines your content**] to match the roles you want.
- :blue[**Personalized optimization**]: We don’t just tweak wording; we :blue[*strategically align*] your resume to highlight the best version of you.
- :blue[**Keyword-driven enhancements**]: We integrate job posting themes and :blue[*ATS-friendly keywords*] so your resume ranks higher in digital screenings.
- :blue[**Seamless automation**]: Save time and energy—:blue[*paste the job description*], and REACT handles the rest.
- :blue[**Tailored experience descriptions**]: Instead of generic bullet points, we :blue[*enhance your work history*] to reflect your qualifications for each role.
- :blue[**AI-powered applications**]: REACT doesn’t stop at your resume—:blue[*it generates custom cover letters and hiring manager messages*] that make your application stand out.

Your resume shouldn’t be static—it should :blue[*adapt and evolve*] with your career. :blue[**Let REACT do the work, so you can focus on landing the job**].

"""


def stream_copy():
    for word in about_copy.split(" "):
        yield word + " "
        time.sleep(0.02)

st.write_stream(stream_copy)