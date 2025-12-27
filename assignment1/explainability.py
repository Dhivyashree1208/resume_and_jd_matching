import numpy as np

def get_top_matching_skills(vectors, vectorizer, top_n=8):
    """
    Extracts top overlapping skills/keywords
    """
    feature_names = vectorizer.get_feature_names_out()

    resume_vec = vectors[0].toarray()[0]
    jd_vec = vectors[1].toarray()[0]

    contribution = resume_vec * jd_vec

    top_indices = np.argsort(contribution)[-top_n:]
    top_skills = [feature_names[i] for i in top_indices if contribution[i] > 0]

    return top_skills
