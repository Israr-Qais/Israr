
# 🌐 Streamlit Sidebar Navigation
st.set_page_config(page_title="AI Resume Shortlister", layout="centered")
st.sidebar.title("📂 Navigation")
page = st.sidebar.radio("Go to", ["Single Resume Match", "Bulk Match + Job Suggestion"])

st.title("🤖 AI Resume Shortlister")

# -----------------------
# 1️⃣ SINGLE MATCH PAGE
# -----------------------
if page == "Single Resume Match":
    st.markdown("Upload a **PDF resume** and enter a **job description** to get:")
    st.markdown("- ✅ AI match score")
    st.markdown("- 🧠 Strengths & improvements")
    st.markdown("- ❌ Missing keywords")
    st.markdown("- 📄 Downloadable report")
    st.markdown("---")

    uploaded_pdf = st.file_uploader("📎 Upload Resume (PDF)", type="pdf")
    job_description = st.text_area("🧾 Paste Job Description")

    if st.button("Evaluate Match"):
        if uploaded_pdf and job_description:
            resume_text = extract_text_from_pdf(uploaded_pdf)
            with st.spinner("Analyzing resume with AI..."):
                result = evaluate_resume(resume_text, job_description)

            st.subheader("📊 AI Match Result:")
            st.write(result)

            save_log(resume_text, job_description, result)

            st.download_button("📥 Download Result as Text", result, file_name="resume_match_result.txt")
        else:
            st.warning("⚠️ Please upload a resume and enter a job description.")

# -------------------------------
# 2️⃣ BULK + JOB SUGGESTION PAGE
# -------------------------------
elif page == "Bulk Match + Job Suggestion":
    st.markdown("### Upload multiple resumes to:")
    st.markdown("- 📊 Compare all against one job")
    st.markdown("- 🧭 Get AI career/job suggestions")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📂 Bulk Resume Matcher")
        job_bulk = st.text_area("🧾 Paste Job Description for Bulk Matching")
        bulk_pdfs = st.file_uploader("📎 Upload Multiple Resumes", type="pdf", accept_multiple_files=True)
        if st.button("🚀 Bulk Match"):
            if bulk_pdfs and job_bulk:
                for resume_file in bulk_pdfs:
                    st.markdown(f"**📄 {resume_file.name}**")
                    resume_text = extract_text_from_pdf(resume_file)
                    with st.spinner("Analyzing..."):
                        result = evaluate_resume(resume_text, job_bulk)
                    st.code(result)
            else:
                st.warning("Upload resumes and paste job description.")

    with col2:
        st.subheader("🎯 AI Job Suggestions")
        suggest_pdfs = st.file_uploader("📎 Upload Resume(s) for Suggestions", type="pdf", accept_multiple_files=True, key="suggest")
        if st.button("💡 Suggest Jobs"):
            if suggest_pdfs:
                for pdf in suggest_pdfs:
                    resume_text = extract_text_from_pdf(pdf)
                    suggestion_prompt = f"""
                    Based on the following resume, suggest 3-5 suitable job roles or titles in the current job market. Avoid repeating content from the resume.

                    Resume:
                    {resume_text}

                    Job Suggestions:
                    """
                    with st.spinner(f"Analyzing {pdf.name}..."):
                        try:
                            suggestion_response = openai.ChatCompletion.create(
                                model="gpt-3.5-turbo",
                                messages=[{"role": "user", "content": suggestion_prompt}],
                                api_key=api_key
                            )
                            suggestion_text = suggestion_response.choices[0].message["content"]
                            st.markdown(f"**{pdf.name}**")
                            st.success(suggestion_text)
                        except Exception as e:
                            st.error(f"OpenAI Error: {e}")
            else:
                st.warning("Upload at least one resume for suggestions.")