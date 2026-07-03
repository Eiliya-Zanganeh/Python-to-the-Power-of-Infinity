import time

time_1 = time.time()

outputs = []
for i in range(100000):
    outputs.append(i ** 2)

time_2 = time.time()

print(f"for loop {time_2 - time_1}")

time_1 = time.time()

outputs = [i ** 2 for i in range(100000)]

time_2 = time.time()

print(f"list comprehension {time_2 - time_1}")