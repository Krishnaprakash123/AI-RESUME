# 🚀 AI Resume & Portfolio Builder

An AI-powered Resume and Portfolio Generator built using Streamlit and Groq LLM.

This application helps users:
- Generate professional resumes
- Create portfolio content
- Perform ATS (Applicant Tracking System) checks
- Export resumes as PDF

---

## 🛠️ Tech Stack

- Python
- Streamlit
- Groq API (LLaMA 3.1)
- HTML & CSS
- ReportLab / PDF Generator

---

## 📂 Project Structure

```
AI-RESUME-PORTFOLIO-BUILDER/
│
├── app.py
├── requirements.txt
├── README.md
│
├── models/
│   ├── llm.py
│   └── prompt_builder.py
│
├── utils/
│   ├── ats_checker.py
│   ├── pdf_generator.py
│   └── portfolio_generator.py
│
├── static/
│   └── style.css
│
└── templates/
    └── html files
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/ai-resume-portfolio-builder.git
cd ai-resume-portfolio-builder
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Set Groq API Key

On Windows:

```bash
setx GROQ_API_KEY "your_api_key_here"
```

Restart your terminal after setting the key.

---

## ▶️ Run the Application

```bash
python -m streamlit run app.py
```

The app will open in your browser.

---

## 🔐 Environment Variable

Make sure your `llm.py` uses:

```python
api_key = os.getenv("GROQ_API_KEY")
```

Do NOT hardcode your API key.

---

## ✨ Features

- AI-generated resume content
- Portfolio content generation
- ATS score checker
- Download resume as PDF
- Clean and responsive UI

---

## 📌 Future Enhancements

- User authentication
- Database integration
- Multiple resume templates
- Cloud deployment

---

## 👨‍💻 Author

Krishna Prakash Anumula

---

## 📜 License

This project is for educational purposes.
