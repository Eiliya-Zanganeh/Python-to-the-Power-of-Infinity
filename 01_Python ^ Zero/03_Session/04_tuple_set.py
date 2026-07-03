# nums = [1, 2, 'Eiliya']
# names = ('Ali', 'Eiliya', 123)
# names = ('Ali',)

nums = {1, 2, 3, 4, 5, 5, 6, 7, 8}
nums = list(nums)
nums = set(nums)

nums_1 = {1, 2, 3, 4}
nums_2 = {4, 5, 6}
print(nums_1 | nums_2)
print(nums_1 & nums_2)
print(nums_1 - nums_2)
