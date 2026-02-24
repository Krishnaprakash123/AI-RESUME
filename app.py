import streamlit as st
from models.llm import generate_ai_content
from models.prompt_builder import build_prompt
from utils.pdf_generator import create_pdf
from utils.portfolio_generator import generate_portfolio

st.set_page_config(page_title="AI Resume Builder")

st.title("🚀 AI Resume & Portfolio Builder")

name = st.text_input("Full Name")
email = st.text_input("Email")
education = st.text_area("Education")
skills = st.text_area("Skills")
projects = st.text_area("Projects")
target_role = st.text_input("Target Role")

if st.button("Generate"):

    data = {
        "name": name,
        "email": email,
        "education": education,
        "skills": skills,
        "projects": projects,
        "target_role": target_role
    }

    prompt = build_prompt(data)

    with st.spinner("Generating content..."):
        result = generate_ai_content(prompt)

    st.subheader("Generated Resume & Cover Letter")
    st.write(result)

    pdf_file = create_pdf(result)

    with open(pdf_file, "rb") as file:
        st.download_button("Download Resume PDF", file, "AI_Resume.pdf")

    portfolio_file = generate_portfolio(data)

    with open(portfolio_file, "rb") as file:
        st.download_button("Download Portfolio HTML", file, "Portfolio.html")