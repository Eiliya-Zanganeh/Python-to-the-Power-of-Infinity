def check(min_score, *args, **kwargs):
    scores_1 = args
    scores_2 = kwargs.values()
    scores = [*scores_1, *scores_2]
    return [score for score in scores if score > min_score]

args = [18, 17]
kwargs = {
    'score_1': 20,
    'score_2': 15,
    'score_3': 18
}

result = check(15, *args, **kwargs)

print(result)
