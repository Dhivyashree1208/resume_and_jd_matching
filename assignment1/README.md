# Resume–Job Description Matching System

## Overview
This project implements an AI-based system to evaluate how well a candidate’s
resume matches a given job description. The system outputs a match score
(0–100) along with an explainable justification, simulating real-world ATS
screening behavior.

---

## Problem Statement
Given a resume and a job description as text, the goal is to determine:
- How relevant the candidate is for the role
- Why the candidate is or is not a good fit

---

## Text Preprocessing
Both resume and job description texts are cleaned and normalized using:
- Lowercasing
- Removal of special characters and formatting noise
- Stopword removal
- Lemmatization
- Whitespace normalization

This ensures matching focuses on meaningful skills rather than formatting.

---

## Feature Engineering (Traditional NLP)
The system uses the following traditional NLP techniques:
- **TF-IDF** for text representation
- **Cosine similarity** to measure overall relevance
- **Skill weighting** to emphasize critical hiring skills
- **Domain keyword alignment** to capture problem relevance

These techniques are interpretable, deterministic, and well-suited for
resume screening tasks.

---

## Scoring Logic
The final match score is calculated using weighted components:

Final Score =
0.3 × TF-IDF similarity +
0.6 × Skill overlap score +
0.1 × Domain alignment bonus

Scores are mapped to:
- Weak Match
- Moderate Match
- Strong Match

This conservative design reflects real ATS filtering behavior.

---

## Evaluation
The system was evaluated using synthetic and realistic resume–JD pairs
covering weak, moderate, and strong match scenarios. Cosine similarity
was chosen due to the absence of labeled hiring data.

---

## Explainability
For each prediction, the system highlights:
- Matched skills
- Domain alignment
- Match category (Weak/Moderate/Strong)

This makes decisions human-readable and auditable.

Decision thresholds were calibrated based on observed score distributions
during testing. Since the scoring model is intentionally conservative,
scores between 35–40 represent strong alignment for intern-level profiles
and are treated as "Hold" rather than rejection.


---

## Assumptions
- Resume and job description are provided as plain text
- Skill presence is a strong indicator of relevance
- No labeled hiring data is available

---

## Limitations
- Does not capture deep semantic similarity
- Skill synonyms are not automatically mapped
- Experience duration is not weighted

---

## Future Improvements
- Sentence embeddings for semantic similarity
- Skill ontology mapping
- Section-wise resume weighting
- Feedback-based learning

---

## Note on Scoring Behavior
The scoring system is intentionally conservative. Due to capped skill and
domain contributions and the nature of TF-IDF cosine similarity on short
texts, scores typically range between 0 and 40 for intern-level profiles.
Higher scores require significantly deeper domain alignment.

This design prevents false positives and reflects real-world ATS screening
behavior.


## How to Run
```bash
pip install -r requirements.txt
python -m assignment1.main
