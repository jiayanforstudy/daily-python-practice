from study_utils import get_valid_scores,calculate_average

def main():
    pages = [
        {"page": 1, "score": 0.32},
        {"page": 2, "score": 0.71},
        {"page": 3}
        # {"page": 1},
        # {"page": 2},
       
    ]
    scores = get_valid_scores(pages)
    average = calculate_average(scores)

    print(scores)
    print(average)

if __name__ == "__main__":
    main()