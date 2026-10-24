pages = [
    {"page": 1, "score": 0.32},
    {"page": 2, "score": 0.71},
    {"page": 3},
    {"page": 4, "score": 0.21},
    {"page": 5, "score": 0.85}
]
# pages = [
#     {"page": 1},
#     {"page": 2, "score": 0.2}
# ]

def get_failed_pages(pages, threshold):
    failed_pages = []

    for page in pages:
        if "score" in page:
            score = page["score"]
            if score < threshold :
                failed_pages.append(page["page"])


    return failed_pages

result = get_failed_pages(pages,0.4)
print(result)