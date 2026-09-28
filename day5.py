def calculate_score(features):
    score = (
    features["overlap_ratio"] * 0.4
    + features["orphan_ratio"] * 0.3
    + features["fragment_ratio"] * 0.3
)
    return score

features = {
    "overlap_ratio" : 0.20,
    "orphan_ratio" : 0.10,
    "fragment_ratio" : 0.30
}

result = calculate_score(features)

print("Page score:", result)
# print(features)

# score = (
#     features["overlap_ratio"] * 0.4
#     + features["orphan_ratio"] * 0.3
#     + features["fragment_ratio"] * 0.3
# )

# print("Page score:", score)