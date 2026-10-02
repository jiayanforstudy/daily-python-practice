def calculate_score(features):
    score = (
        features["overlap_ratio"] * 0.4
        + features["orphan_ratio"] * 0.3
        + features["fragment_ratio"] * 0.3
    )
    return score

def evaluate_page(features):
    if features["overlap_ratio"] > 0.6:
        return "FALL" #return作用：一旦执行到这里，整个函数马上结束。

    score = calculate_score(features)
    if score > 0.4 :
        return "FALL"
    else:
        return "PASS"

features = {
    "overlap_ratio": 0.5,
    "orphan_ratio": 0.5 ,
    "fragment_ratio": 0.5
}

result = evaluate_page(features)
print("Result:",result)
