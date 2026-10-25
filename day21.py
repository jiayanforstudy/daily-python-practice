# pages = [
#     {"page": 1, "score": 0.32},
#     {"page": 2, "score": 0.71},
#     {"page": 3},
#     {"page": 4, "score": 0.21},
#     {"page": 5, "score": 0.85}
# ]
pages = []

def count_failed_pages(pages, threshold):
    count = 0

    for page in pages:
        if "score" in page:
            score = page["score"]

            if score > threshold:
                count = count + 1

    return count

result = count_failed_pages(pages,0.4)

print(result)