# 🤖 AI Resume Shortlister + Job Matcher

An AI-powered Streamlit app that analyzes resumes, scores candidates, and suggests job roles using OpenAI's GPT-3.5 Turbo.

---

## 🚀 Features

- 📎 Upload **single or multiple PDF resumes**
- 🧠 Get **AI-generated match scores, strengths & improvement suggestions**
- ❌ Detect **missing keywords** for job fit
- 🎯 Generate **AI Job Suggestions** based on resume content
- 📥 Downloadable match reports
- 📊 CSV logging for results
- 🧭 Streamlit sidebar navigation

---

## 🖼️ Demo

📹 *[Insert video demo link here]*  
🖼️ Screenshot:

![screenshot](./screenshot.png)

---

## ⚙️ How to Run Locally

```bash
# Clone this repository
git clone https://github.com/your-username/ai-resume-shortlister.git
cd ai-resume-shortlister

# Install dependencies
pip install -r requirements.txt

# Create .env file
echo OPENAI_API_KEY="your-key-here" > .env

# Run the app
streamlit run resume_shortlister.py
