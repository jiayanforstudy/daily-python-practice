words = ["rag", "agent", "rag", "llm", "agent", "rag"]


def count_words(words):
    count = {}
    
    for word in words:
        if word in count:
            count[word] = count[word] + 1
        else:
            count[word] = 1

    sorted_score = sorted(
        count.items(),
        key = lambda x:x[1],
        reverse=True
    )
    max_count_word = sorted_score[0]
    return max_count_word

result = count_words(words)
print(result)

