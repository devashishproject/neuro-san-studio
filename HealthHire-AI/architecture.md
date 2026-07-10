# HealthHire AI Architecture

## Project Overview

HealthHire AI is a Healthcare Resume Analyzer built using a Neuro SAN multi-agent architecture.

The solution helps healthcare recruiters and healthcare organizations automate resume screening, identify healthcare-specific skills, match candidates to suitable healthcare roles, detect skill gaps, and provide career recommendations.

---

## Problem Statement

Healthcare organizations receive a large number of resumes for roles such as:

- Medical Coder
- Clinical Research Associate
- Healthcare Analyst
- Medical Billing Specialist
- Healthcare Administrator

Manual screening is time-consuming and can lead to inconsistent evaluations.

HealthHire AI automates this process using specialized AI agents.

---

## Multi-Agent Architecture

### Agent 1: Resume Extraction Agent

Responsibilities:

- Read resume content
- Extract candidate information
- Identify experience
- Extract educational qualifications
- Extract certifications

Output:

- Candidate Profile

---

### Agent 2: Healthcare Skills Agent

Responsibilities:

- Identify healthcare-specific skills
- Detect healthcare certifications
- Validate healthcare terminology

Skills Detected:

- ICD Coding
- CPT Coding
- HIPAA
- Clinical Documentation
- EMR
- EHR
- Healthcare Analytics

Output:

- Healthcare Skill Profile

---

### Agent 3: Job Matching Agent

Responsibilities:

- Compare candidate skills with healthcare roles
- Determine the best matching job role
- Generate candidate match score

Output:

- Recommended Job Role
- Match Percentage

---

### Agent 4: Gap Analysis Agent

Responsibilities:

- Identify missing healthcare skills
- Identify missing certifications
- Highlight knowledge gaps

Output:

- Skill Gap Report

---

### Agent 5: Recommendation Agent

Responsibilities:

- Recommend healthcare certifications
