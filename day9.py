results = [
    {"doc_id": "A", "score": 0.82},
    {"doc_id": "B", "score": 0.75},
    {"doc_id": "A", "score": 0.91},
    {"doc_id": "C", "score": 0.68},
    {"doc_id": "B", "score": 0.80}
]

best_scores = {}

for item in results:
    doc_id = item["doc_id"]
    score = item["score"]

    if doc_id not in best_scores:
        best_scores[doc_id] = score
    else:
        if score > best_scores[doc_id]:
            best_scores[doc_id] = score

print(best_scores)

sorted_scores = sorted(
    best_scores.items(),
    key=lambda x: x[1],
    reverse=True
)
top2 = sorted_scores[:2]

print("sorted:",sorted_scores)
print("top2:",top2)

# dict.items()   → 把字典变成一组 (key, value)
# sorted()       → 排序
# reverse=True   → 从大到小
# [:2]           → 取前两个