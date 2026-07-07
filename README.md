# Resume AI Pipeline

## Overview

Resume AI Pipeline is an AI-powered system that automatically tailors a master resume to a specific job description.

The project extracts structured information from a job posting, analyzes a master resume, calculates the degree of alignment, and generates an optimized resume focused on maximizing ATS compatibility.

---

## Project Goals

- Parse job descriptions.
- Parse master resumes.
- Extract structured JSON.
- Match candidate profile against job requirements.
- Optimize resume.
- Generate cover letters.
- Generate interview preparation material.

---

## Current Status

Current Sprint:

Sprint 0 — Job Parser Stabilization

Current Provider:

- Google Gemini

---

## Architecture

```
Input Files
     │
     ▼

Job Parser
     │

Resume Parser
     │

Matching Engine
     │

Resume Optimizer
     │

Cover Letter Generator
     │

Interview Assistant
```

---

## Technologies

- Python
- Google Gemini API
- JSON Schema
- PyMuPDF
- python-docx
- Pandas

---

## Project Structure

```
resume-ai/

│
├── app.py
├── config.py
├── requirements.txt
├── .env
│
├── modules/
├── prompts/
├── schemas/
├── input/
├── output/
├── tests/
└── docs/
```

---

## Installation

```bash
python -m venv .venv

pip install -r requirements.txt
```

---

## Current Roadmap

- Sprint 0
    - Job Parser

- Sprint 1
    - Resume Parser

- Sprint 2
    - Matching Engine

- Sprint 3
    - Resume Optimizer

- Sprint 4
    - Cover Letter Generator

- Sprint 5
    - Interview Assistant

---

## License

MIT License