def extract_resume_information(text):
    skills = []

    healthcare_keywords = [
        "ICD",
        "CPT",
        "HIPAA",
        "EMR",
        "EHR",
        "Medical Coding",
        "Clinical Documentation",
        "Healthcare Analytics"
    ]

    for skill in healthcare_keywords:
        if skill.lower() in text.lower():
            skills.append(skill)

    return {
        "detected_skills": skills
    }
`