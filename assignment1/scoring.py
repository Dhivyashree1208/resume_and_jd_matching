from sklearn.metrics.pairwise import cosine_similarity
from assignment1.preprocessing import preprocess_text
from assignment1.feature_engineering import get_tfidf_vectors

# Core skills that strongly influence hiring decisions
IMPORTANT_SKILLS = [
    "python",
    "machine learning",
    "ml",
    "nlp",
    "data analysis",
    "deep learning"
]

# Domain-level keywords to capture problem relevance
DOMAIN_KEYWORDS = [
    "tf-idf",
    "cosine similarity",
    "text classification",
    "resume screening",
    "feature engineering",
    "data preprocessing",
    "machine learning",
    "nlp"
]


def skill_overlap(resume_raw: str, jd_raw: str):
    """
    Detect important skill overlap using raw text
    (preserves multi-word skills)
    """
    resume_text = resume_raw.lower()
    jd_text = jd_raw.lower()

    matched_skills = []

    for skill in IMPORTANT_SKILLS:
        if skill in resume_text and skill in jd_text:
            matched_skills.append(skill)

    return matched_skills


import re

def domain_alignment_bonus(resume_raw: str, jd_raw: str):
    resume_text = re.sub(r'\s+', ' ', resume_raw.lower())
    jd_text = re.sub(r'\s+', ' ', jd_raw.lower())

    matches = 0
    for keyword in DOMAIN_KEYWORDS:
        if keyword in resume_text and keyword in jd_text:
            matches += 1

    return min(matches * 5, 20)


def calculate_match_score(resume_text: str, jd_text: str):
    """
    Calculates final resume–JD match score (0–100)
    using explainable weighted logic
    """

    # ---------- Preprocessing ----------
    resume_clean = preprocess_text(resume_text)
    jd_clean = preprocess_text(jd_text)

    # ---------- Feature Engineering ----------
    vectors, vectorizer = get_tfidf_vectors(resume_clean, jd_clean)

    # ---------- Similarity ----------
    similarity = cosine_similarity(vectors[0], vectors[1])[0][0]
    similarity_score = similarity * 100  # scale to 0–100

    # ---------- Skill Scoring ----------
    matched_skills = skill_overlap(resume_text, jd_text)
    skill_score = min(len(matched_skills) * 20, 60)

    # ---------- Domain Bonus ----------
    domain_bonus = domain_alignment_bonus(resume_text, jd_text)

    # ---------- Final Weighted Score ----------
    final_score = round(
        (0.3 * similarity_score) +
        (0.6 * skill_score) +
        (0.1 * domain_bonus),
        2
    )

    return final_score, vectors, vectorizer, matched_skills
