nums = [1, 2, 3, 4, 5, 6, 7, 8]

# def pow(n):
#     return n ** 2

# pow = lambda n: n ** 2

outputs = map(lambda n: n ** 2, nums)
outputs = list(outputs)
print(outputs)

# outputs = [num ** 2 for num in nums]