names = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

# [start:end:step]


print(names[1:4])
print(names[:4]) # => names[0:4]
print(names[4:]) # => names[4:9], names[4:-1]

print(names[::2])