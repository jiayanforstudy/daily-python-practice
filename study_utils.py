def get_valid_scores(pages):
    scores = []

    for page in pages:
        if "score" in page:
            scores.append(page["score"])
    return scores

 