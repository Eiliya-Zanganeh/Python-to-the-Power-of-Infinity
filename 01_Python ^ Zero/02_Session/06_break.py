sum_scores = 0
scores_count = 0

while True:
    score = input("Enter your score ( q for quit ): ")

    if score == 'q':
        break
    else:
        score = float(score)

    scores_count += 1
    sum_scores += score

print(f"Result: {sum_scores / scores_count}")

