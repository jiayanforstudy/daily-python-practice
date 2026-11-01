pages = [
    {"page": 1, "score": 0.32},
    {"page": 2, "score": 0.71},
    {"page": 3},
    {"page": 4, "score": 0.21},
    {"page": 5, "score": 0.85},
    {"page": 6, "score": 0.15},
    {"page": 7, "score": 0.56},
    {"page": 8, "score": 0.40},
    {"page": 9}
]
# pages = []
# pages = [
#     {"page": 1},
#     {"page": 2}
# ]

def get_valid_pages(pages):
    valid_count = 0
    page_count = 0
    average_score = 0
    total_score = 0


    for page in pages:
        if "score" in page:
            valid_count = valid_count + 1
            page_count = page_count + 1
            score = page.get("score")
            total_score = total_score + score
    
    if page_count == 0:#注意边界情况
        average_score = 0
    else:
        average_score = total_score / page_count

    return valid_count,average_score

def analyze_pages(pages, threshold):
    
    failed_pages = []
    worst_3 = []
    valid_pages = []
    sorted_pages = []

    for page in pages:
        if "score" in page:
            score = page.get("score")
            valid_pages.append(page)
            if score < threshold:
                failed_pages.append(page["page"])

    sorted_pages = sorted(
        valid_pages,
        key=lambda x:x["score"]
    )
    worst_3 = sorted_pages[:3]
    
    valid_count, average_score = get_valid_pages(pages)#注意写法

    result = {
        "valid_count": valid_count,
        "average_score": average_score,
        "failed_pages": failed_pages,
        "worst_3": worst_3
    }
    return result

result = analyze_pages(pages,0.4)
print(result)

