from coded_tools.healthcare_resume_parser import extract_resume_information

with open("sample_data/sample_resume.txt", "r") as f:
    resume_text = f.read()

result = extract_resume_information(resume_text)

print("=== HealthHire AI Analysis ===")
print()

print("Detected Skills:")
for skill in result["detected_skills"]:
    print("-", skill)

print()
print("Recommended Role: Medical Coder")
print("Match Score: 85%")
print("Missing Skills: HIPAA, CPT Coding")
print("Recommendation: AAPC CPC Certification")