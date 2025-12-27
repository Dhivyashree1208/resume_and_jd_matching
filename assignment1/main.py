from assignment1.scoring import calculate_match_score
from assignment1.evaluation import evaluate_match

# -------------------------
# Sample Resume Text
# -------------------------
resume_text = """
AI/ML intern with strong hands-on experience in Python, Machine Learning,
and Natural Language Processing. Built multiple end-to-end NLP systems
focused on resume screening, text classification, and similarity-based
matching.

Implemented TF-IDF and cosine similarity for document matching and
candidate screening. Worked extensively on data preprocessing, feature
engineering, and NLP pipelines using scikit-learn and NLTK.

Developed and evaluated ML models, optimized preprocessing pipelines,
and analyzed results. Familiar with complete ML workflows, data
structures, and applied machine learning concepts.
"""



jd_text = """
We are hiring an AI/ML Intern with strong proficiency in Python and Machine
Learning. The candidate will work on resume screening, text classification,
and NLP-based similarity matching systems.

Required experience includes implementing TF-IDF and cosine similarity,
working on data preprocessing and feature engineering, and building NLP
pipelines using libraries such as scikit-learn and NLTK.

Strong understanding of machine learning workflows and applied ML
techniques is expected.
"""


score, vectors, vectorizer, matched_skills = calculate_match_score(
    resume_text, jd_text
)

match_type = evaluate_match(score)

# -------------------------
# Output
# -------------------------
print("Match Score:", score)
print("Match Type:", match_type)
print("Key Matching Skills:", matched_skills)