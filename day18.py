from study_utils import get_valid_scores


def main():
    pages = [
        {"page":1,"score":0.32},
        {"page":2,"score":0.71},
        {"page":3}
    ]

    result = get_valid_scores(pages)

    print(result)


if __name__ =="__main__":
    main()
