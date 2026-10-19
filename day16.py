pages = [
    {"page":1, "score":0.32},
    {"page":2, "score":0.71},
    {"page":3}
]

def get_valid_scores(pages):
    scores = []

    for page in pages:
        if "score" in page:
            score = page["score"]

            scores.append(score)

    return scores


result = get_valid_scores(pages)
print(result)

#默认有score，真的缺了再异常处理；能预判正常分支，用if；真正异常的情况，用try/except
# try:
#     score = page["score"]
#     scores.append(score)
# except KeyError
#     pass