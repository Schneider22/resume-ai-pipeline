from modules.validator import JsonValidator

validator = JsonValidator("schemas/job_schema.json")

data = {
    "job_title": "Senior Data Engineer",
    "company": "OpenAI",
    "location": "Remote",
    "employment_type": "Full Time",
    "experience_level": "Senior",
    "industry": "Artificial Intelligence",
    "summary": "Design and maintain modern data platforms.",

    "responsibilities": [
        "Build ETL pipelines",
        "Optimize SQL queries"
    ],

    "required_skills": [
        "Python",
        "SQL",
        "AWS"
    ],

    "preferred_skills": [
        "Spark",
        "Docker"
    ],

    "required_tools": [
        "Git",
        "Airflow"
    ],

    "soft_skills": [
        "Communication",
        "Leadership"
    ],

    "education": [
        "Bachelor's Degree"
    ],

    "languages": [
        "English"
    ],

    "certifications": [
        "AWS Certified Data Engineer"
    ],

    "keywords": [
        "Python",
        "ETL",
        "Data Engineering"
    ]
}

try:

    validator.validate(data)

    print("Schema OK")

except Exception as ex:

    print(ex)