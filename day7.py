def calculate_score(features):
    score = (
        features["overlap_ratio"] * 0.4
        + features["orphan_ratio"] * 0.3
        + features["fragment_ratio"] * 0.3
    )
    return score

def evaluate_page(features):
    if features["overlap_ratio"] > 0.6:
        return "FALL"
    score = calculate_score(features)

    if score > 0.4:
        return "FALL"
    else:
        return "PASS"


pages = [
    {"overlap_ratio": 0.2,
     "orphan_ratio": 0.1,
     "fragment_ratio":0.3
     },
    {"overlap_ratio": 0.8,
     "orphan_ratio": 0.1,
     "fragment_ratio":0.2
    },
    {"overlap_ratio": 0.3,
     "orphan_ratio": 0.2,
     "fragment_ratio":0.4
    }
]
fail_count = 0
page_number = 1

for page in pages:
    result = evaluate_page(page)
    print("Page",page_number,":",result)

    if result == "FALL" :
        fail_count = fail_count + 1

    page_number = page_number + 1

if fail_count >= 1:
    print("Document result: FALL")
else:
    print("Document result: PASS")
