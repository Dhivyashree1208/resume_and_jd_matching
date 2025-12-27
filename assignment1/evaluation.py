def evaluate_match(score):
    """
    Categorizes match quality
    """
    if score >= 50:
        return "Strong Match"
    elif score >= 30:
        return "Moderate Match"
    else:
        return "Weak Match"
