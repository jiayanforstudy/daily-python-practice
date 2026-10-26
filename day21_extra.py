# pages = [
#     {"page": 1, "score": 0.32},
#     {"page": 2, "score": 0.71},
#     {"page": 3},
#     {"page": 4, "score": 0.21},
#     {"page": 5, "score": 0.85},
#     {"page": 6, "score": 0.15},
#     {"page": 7, "score": 0.56},
#     {"page": 8}
# ]

# pages = []
pages = [
    {"page": 1},
    {"page": 2},
    {"page": 3},
    {"page": 4},
    {"page": 5},
    {"page": 6},
    {"page": 7},
    {"page": 8}
]
def analyze_pages(pages, threshold):
    total_pages = len(pages)
    valid_pages = 0
    failed_count = 0
    failed_pages = []
    failure_rate = 0

    for page in pages:

        if "score" in page:
            valid_pages = valid_pages + 1
            score = page["score"]

            if score < threshold:
                failed_count = failed_count + 1
                failed_pages.append(page["page"])
    
    if valid_pages > 0:
        failure_rate = failed_count / valid_pages * 100
    else:
        failure_rate = 0

    result = {
        "total_pages":total_pages,
        "valid_pages": valid_pages,
        "failed_count": failed_count,
        "failed_pages": failed_pages,
        "failure_rate": failure_rate
    }    
    return result

result = analyze_pages(pages,0.4)
print(result)


