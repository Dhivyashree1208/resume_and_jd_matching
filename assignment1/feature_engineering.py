from sklearn.feature_extraction.text import TfidfVectorizer

def get_tfidf_vectors(resume_text, jd_text):
    """
    Converts resume and JD into TF-IDF vectors
    """
    vectorizer = TfidfVectorizer(
    ngram_range=(1, 1),   
    max_df=0.85,
    min_df=1
)


    vectors = vectorizer.fit_transform([resume_text, jd_text])

    return vectors, vectorizer
