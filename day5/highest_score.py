all_scores = input("Type all scores seperated by a comma: ").split(",")

for n in range(0, len(all_scores)):
    all_scores[n] = int(all_scores[n])

all_scores_sorted = sorted(all_scores)
print(all_scores_sorted)

high_score = all_scores_sorted[-1]

print(high_score)