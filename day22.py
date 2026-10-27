from day21_extra import analyze_pages

pages = [
    {"page": 1, "score": 0.32},
    {"page": 2, "score": 0.71},
    {"page": 3},
    {"page": 4, "score": 0.21},
    {"page": 5, "score": 0.85},
    {"page": 6, "score": 0.15},
    {"page": 7, "score": 0.56},
    {"page": 8}
]
# pages = []

result = analyze_pages(pages,0.4)

assert result["total_pages"] == 8
assert result["valid_pages"] == 6
assert result["failed_count"] == 3
assert result["failed_pages"] == [1,4,6]

empty_result = analyze_pages([], 0.4)
assert empty_result["total_pages"] == 0
assert empty_result["failure_rate"] == 0

print("All tests passed!")
