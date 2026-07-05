scores = [20, 18, 17, 15, 14]
result = filter(lambda score: score >= 18, scores)
result = list(result)
print(result)