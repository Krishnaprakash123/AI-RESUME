import re
from collections import Counter

# -----------------------------
# Text Cleaning Function
# -----------------------------
def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    return text


# -----------------------------
# Extract Keywords
# -----------------------------
def extract_keywords(text):
    words = clean_text(text).split()
    
    # Remove common stopwords
    stopwords = {
        "the", "is", "in", "and", "to", "of", "for", "with",
        "a", "an", "on", "at", "by", "from", "as", "that",
        "this", "be", "are", "or", "your", "you"
    }

    keywords = [word for word in words if word not in stopwords and len(word) > 2]
    return keywords


# -----------------------------
# ATS Match Score Calculator
# -----------------------------
def calculate_ats_score(resume_text, job_description):
    resume_keywords = extract_keywords(resume_text)
    job_keywords = extract_keywords(job_description)

    resume_counter = Counter(resume_keywords)
    job_counter = Counter(job_keywords)

    matched_keywords = []
    missing_keywords = []

    for word in job_counter:
        if word in resume_counter:
            matched_keywords.append(word)
        else:
            missing_keywords.append(word)

    if len(job_counter) == 0:
        return 0, [], []

    score = (len(matched_keywords) / len(job_counter)) * 100
    score = round(score, 2)

    return score, matched_keywords, missing_keywords


# -----------------------------
# Suggest Improvements
# -----------------------------
def get_suggestions(score, missing_keywords):
    if score >= 80:
        message = "Excellent ATS match! Your resume is well optimized."
    elif score >= 60:
        message = "Good match. Consider adding more relevant keywords."
    else:
        message = "Low ATS match. You should improve keyword alignment."

    suggestions = f"""
    ATS Score: {score}%

    Suggestions:
    - Include these missing keywords if relevant:
      {', '.join(missing_keywords[:10])}
    - Add measurable achievements.
    - Use action verbs like Developed, Implemented, Designed.
    - Keep formatting simple (avoid tables & images).
    """

    return message, suggestions