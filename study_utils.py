def get_valid_scores(pages):
    scores = []

    for page in pages:
        if "score" in page:
            scores.append(page["score"])
    return scores


def calculate_average(scores):
    if not scores:
        return 0
    
    total = 0

    for score in scores:
        total = total + score

    average = total / len(scores)

    return average
