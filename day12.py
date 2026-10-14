pages = [
    {"page": 1, "score": 0.32},
    {"page": 2, "score": 0.71},
    {"page": 3, "score": 0.48},
    {"page": 4, "score": 0.21},
]


def analyze_document(pages):
    total_pages = len (pages)
    
    total_score = 0
    fail_pages = 0
    max_score = 0
    best_page = None
    
    for page in pages:
        score = page["score"]
        total_score = total_score + score

        if score < 0.4:
            fail_pages = fail_pages + 1

        if score > max_score:
            max_score = score
            best_page = page["page"]
    avg_score = total_score / total_pages

    result = {
        "total_pages" : total_pages,
        "avg_score" : avg_score,
        "fail_pages" : fail_pages,
        "best_page" : best_page
    }
    
    return result

result = analyze_document(pages)
print(result)