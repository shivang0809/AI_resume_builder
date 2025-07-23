import streamlit as st
import openai

# Set your OpenAI API key here
openai.api_key = "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"

st.set_page_config(page_title="AI Resume Generator", layout="centered")
st.title("🤖 AI Resume & Cover Letter Generator")

with st.form("resume_form"):
    name = st.text_input("Your Name")
    job_role = st.text_input("Job Role")
    experience = st.number_input("Years of Experience", min_value=0, step=1)
    skills = st.text_input("Skills (comma-separated)")
    goal = st.text_area("Career Goal")
    job_desc = st.text_area("Target Job Description (optional)")

    submitted = st.form_submit_button("Generate")

if submitted:
    with st.spinner("Generating resume summary..."):
        summary_prompt = f"""Write a professional resume summary for {name}, a {job_role} with {experience} years of experience. Skills: {skills}. Career goal: {goal}"""
        summary_response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": summary_prompt}]
        )
        summary = summary_response['choices'][0]['message']['content']

    with st.spinner("Generating cover letter..."):
        cover_letter_prompt = f"""Write a personalized cover letter for a {job_role} role. Candidate: {name}, with {experience} years of experience. Skills: {skills}. Career goal: {goal}. Target job description: {job_desc}"""
        cover_letter_response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": cover_letter_prompt}]
        )
        cover_letter = cover_letter_response['choices'][0]['message']['content']

    st.subheader("📄 Resume Summary")
    st.write(summary)

    st.subheader("📝 Cover Letter")
    st.write(cover_letter)