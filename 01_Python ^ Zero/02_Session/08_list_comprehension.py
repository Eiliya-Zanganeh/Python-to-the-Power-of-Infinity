# output = []
#
# for i in range(10):
#     output.append(i ** 2)
#
# print(output)

# output = [i ** 2 for i in range(10)]
# print(output)


# output = []
#
# for i in range(1, 11):
#     output.append('*' * i)
#
# print(output)

# output = ['*' * i for i in range(1, 11)]
# print(output)

# output = []
#
# for i in range(20):
#     if i % 2 == 0:
#         output.append(i)
#
# print(output)

output = [i for i in range(20) if i % 2 == 0]
print(output)

password = '123'

text = 'Welcome' if password == '123' else password