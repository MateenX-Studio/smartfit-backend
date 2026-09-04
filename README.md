# SmartFit AI - Backend

FastAPI backend for SmartFit AI, an AI-powered CV analyzer that matches resumes against job descriptions.

## Features
- Multi-format CV upload (PDF, DOCX, PPTX)
- AI-powered analysis using Google Gemini (match score, missing skills, suggestions, role recommendations)
- User authentication (signup/login) via Supabase Auth
- Analysis history stored per user
- Automatic token refresh
- Retry logic for AI service reliability

## Tech Stack
- Python
- FastAPI
- Google Gemini API
- Supabase (Auth + Database)
- PyPDF, python-docx, python-pptx

## Run locally
```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

## Environment variables required
Create a `.env` file with:
GEMINI_API_KEY=your_key
SUPABASE_URL=your_url
SUPABASE_KEY=your_key


## Made by
MateenX-Studio