scores = [0.2, 0.5, 0.9, 0.3, 0.6]

total = 0

for score in scores:
    print(score)
    total = total + score

average = total / len(scores)

print("Average:" , average)
