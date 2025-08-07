import streamlit as st
import requests

st.title("📄 Smart Resume Analyzer & Enhancer (FLAN-T5)")
st.write(
    "Upload your resume and paste a job description. "
    "The AI will score and optionally enhance it."
)

resume_file = st.file_uploader("Upload your Resume (PDF only)", type=["pdf"])
job_description = st.text_area("Paste Job Description here")
enhance = st.checkbox("Enhance Resume with AI")

if st.button("Analyze Resume") and resume_file and job_description:
    with st.spinner("Analyzing..."):
        response = requests.post(
            "http://localhost:8000/analyze",
            files={"resume": resume_file},
            data={"job_description": job_description, "enhance": enhance}
        )

        if response.status_code == 200:
            data = response.json()
            st.success(f"Resume Match Score: {data['score']}%")
            st.subheader("Insights:")
            missing_keywords = (
                ', '.join(data['insights']['missing_keywords']) or 'None'
            )
            st.write(f"Missing Keywords: {missing_keywords}")
            if enhance:
                st.subheader("AI-Enhanced Resume:")
                st.text_area(
                    "Enhanced Resume",
                    data["rewritten_resume"],
                    height=300
                )
        else:
            st.error("Failed to process the resume.")
