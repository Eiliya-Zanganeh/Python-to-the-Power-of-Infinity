import pandas as pd

scores = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9])

print(scores)
print(type(scores))

scores = scores.values

print(type(scores))