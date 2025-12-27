def get_decision(score: float):
    """
    Decision thresholds based on match score
    """
    if score >= 60:
        return "Shortlist", "High"
    elif score >= 30:
        return "Hold", "Medium"
    else:
        return "Reject", "Low"
