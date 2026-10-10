results = [
    {"doc_id": "A", "score": 0.82},
    {"doc_id": "B", "score": 0.75},
    {"doc_id": "A", "score": 0.91},
    {"doc_id": "C", "score": 0.68},
    {"doc_id": "B", "score": 0.80}
]

best_scores = {}

def get_top_docs(results, k):

    best_scores = {} #封装函数的时候变量要写在里面（不应该依赖外部变量）
    for item in results:
        doc_id = item["doc_id"]
        score = item["score"]

        if doc_id not in best_scores:
            best_scores[doc_id] = score
        else:
            if score > best_scores[doc_id]:
                best_scores[doc_id] = score

    sorted_score = sorted(
        best_scores.items(),#items让key和value都保留
        key=lambda x:x[1],
        reverse=True
    )
    top_docs = sorted_score[:k]
    return top_docs

top_docs = get_top_docs(results, 2)
print(top_docs)