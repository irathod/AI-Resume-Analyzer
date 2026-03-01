# AI Resume Analyzer

A web-based ATS-style resume screening tool built using Flask.

## Features
- Upload PDF resume
- Extract technical skills
- Compare with job description
- Calculate match score
- Display matching and missing skills

## Tech Stack
- Python
- Flask
- Gunicorn
- HTML/CSS
- Regex-based skill extraction

## Live Demo
[Click Here]((https://ai-resume-analyzer-2gtb.onrender.com))

## How It Works
The system extracts predefined technical skills from both the resume and the job description using regex-based word matching. The match score is calculated as:

Match Score = (Matched Skills / Required Skills) × 100
