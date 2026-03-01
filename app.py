from flask import Flask, render_template, request
from PyPDF2 import PdfReader
import re

app = Flask(__name__)

# Simple Clean Skill Database
SKILLS_DB = [
    "python","java","c++","sql","mysql","mongodb",
    "html","css","javascript","react","node",
    "express","flask","django","tensorflow","pandas",
    "numpy","machine learning","nlp","aws","docker",
    "git","github","rest api","data structures","algorithms"
]

def extract_text_from_pdf(file):
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text
    return text.lower()

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/analyze', methods=['POST'])
def analyze():

    # Check resume upload
    file = request.files.get('resume')
    if not file or file.filename == "":
        return "Please upload a resume."
    if not file.filename.lower().endswith(".pdf"):
        return "Only PDF files are allowed."

    # Extract resume text
    resume_text = extract_text_from_pdf(file)

    # Get job description
    job_description = request.form.get('job_description', "")
    if not job_description.strip():
        return "Please paste a job description."

    job_description = job_description.lower()

    resume_skills = set()
    required_skills = set()

    # Skill matching
    for skill in SKILLS_DB:
        pattern = r'\b' + re.escape(skill) + r'\b'

        if re.search(pattern, resume_text):
            resume_skills.add(skill)

        if re.search(pattern, job_description):
            required_skills.add(skill)

    # If JD has no skills
    if len(required_skills) == 0:
        return "No technical skills detected in Job Description."

    matching_skills = sorted(resume_skills & required_skills)
    missing_skills = sorted(required_skills - resume_skills)

    score = round((len(matching_skills) / len(required_skills)) * 100, 2)

    return render_template("result.html",
                           score=score,
                           matching_skills=matching_skills,
                           missing_skills=missing_skills,
                           total_required=len(required_skills),
                           total_matched=len(matching_skills))

if __name__ == "__main__":
    app.run(debug=True)