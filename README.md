# 🧠 AI Resume Screening System  
**Explainable ATS Scoring | REST API | Flask UI**

This repository contains an end-to-end AI-based resume screening system that
evaluates how well a candidate’s resume matches a given job description.
The project focuses on **explainability, clarity, and real-world hiring relevance**
rather than black-box AI decisions.

The solution is divided into **two core assignments** and **one optional UI layer**.

---

## 📂 Project Structure

<img width="456" height="722" alt="image" src="https://github.com/user-attachments/assets/999f337e-3011-4adc-8ee2-71926eb740d2" />


📌 **Note:**  
Each assignment has its **own README file** explaining implementation details,
design decisions, and trade-offs.

---

## 🧩 Assignment 1: Resume–Job Description Matching (ML Fundamentals)

### Objective
Build an AI-based system that evaluates how well a resume matches a job
description and produces:
- A match score (0–100)
- A clear, human-readable explanation

### Techniques Used
- Text preprocessing (cleaning, normalization, lemmatization)
- TF-IDF vectorization
- Cosine similarity
- Rule-based skill weighting
- Explainable scoring logic

📄 **Detailed explanation:**  
➡️ See [`assignment1/README.md`](assignment1/README.md)

### 🔍 Sample Output (Assignment 1)

<img width="781" height="229" alt="image" src="https://github.com/user-attachments/assets/5c45b05d-8bc4-48e2-b3dc-4c9b109d292d" />
<img width="742" height="222" alt="image" src="https://github.com/user-attachments/assets/3e5b2d7f-951d-44d4-9aaf-845d8725c02e" />

---

## 🧩 Assignment 2: AI Screening Service (System Thinking)

### Objective
Convert the matching logic into a REST API that simulates an
Applicant Tracking System (ATS) screening service.

### Features
- FastAPI-based REST API
- Structured request & response schema
- Decision logic: Shortlist / Hold / Reject
- Edge case handling
- Explainable output

📄 **Detailed explanation:**  
➡️ See [`assignment2/README.md`](assignment2/README.md)

### 🌐 API Demo (Swagger UI)
<img width="1536" height="881" alt="image" src="https://github.com/user-attachments/assets/7b5ae8c2-918f-49e8-af7d-f7225cf1c54b" />

<img width="1529" height="701" alt="image" src="https://github.com/user-attachments/assets/333f2d8b-fa2a-469e-bb01-43d5d6f9db30" />



---

## 🎨 Optional Enhancement: Flask UI (Demo Layer)

A simple Flask-based web interface was added to allow users to:
- Upload resume and job description files (PDF / TXT)
- View ATS match score, decision, and matched skills
- Interact with the system through a single UI

⚠️ This UI **does not modify the core logic** and is intended purely for
demonstration and usability purposes.

### 🖥 Flask UI Screenshot

<img width="1158" height="528" alt="image" src="https://github.com/user-attachments/assets/95aa4d7b-05d9-43ec-a126-382c030d3396" />

<img width="1031" height="645" alt="image" src="https://github.com/user-attachments/assets/de110ac9-ba25-4d25-b3b1-6c8438bd567f" />



---

## 🤖 LLM Usage

Large Language Models (LLMs) were **not used** in the scoring pipeline.

### Reason
- Hiring decisions require deterministic and explainable logic
- Traditional NLP techniques provide transparency and reproducibility
- Avoids hallucination and black-box behavior

LLMs may be explored in future versions for:
- Resume summarization
- Skill normalization
- Non-decision-support tasks

---

## 🏗 Architecture Overview

- **Assignment 1:** Core NLP-based scoring engine
- **Assignment 2:** REST API exposing the scoring logic
- **Flask App:** Optional UI for manual testing and demonstration

The system is modular and suitable for integration into a larger ATS pipeline.

---

## ⚖ Assumptions & Limitations

### Assumptions
- Resume and JD text are provided as plain or extracted text
- Intern-level profiles are evaluated conservatively
- Skill overlap is a key indicator of relevance

### Limitations
- TF-IDF captures lexical similarity, not deep semantics
- No labeled hiring dataset is used
- Conservative thresholds may reject borderline candidates

### Alignment with Assignment Requirements

The assignment emphasizes explainability, realistic scoring, and avoidance
of black-box decisions. The conservative scoring approach ensures:
- Transparent and auditable results
- Reduced false positives
- Clear differentiation between weak, moderate, and strong matches

Rather than optimizing for higher scores, the system focuses on reliable
and explainable evaluation, which satisfies both the technical and system-
thinking objectives of the assignment.


---

## 🚀 How to Run Assignment1,Assignment2,Flask app(optional)

### Install dependencies and run the system
```bash
pip install -r requirements.txt
python -m assignment1.main
uvicorn assignment2.app:app --reload
python flask_app/app.py



