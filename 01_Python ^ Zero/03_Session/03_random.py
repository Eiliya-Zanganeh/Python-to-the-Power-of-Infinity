import random

# print(random.randint(1, 3))
#
# colors = ['red', 'green', 'blue']
# print(random.choice(colors))

items_count = int(input('Enter number of items: '))
items = [input('Enter item: ') for i in range(items_count)]

for i in range(items_count):
    random_index = random.randint(0, len(items))
    random_item = items.pop(random_index)
    print(f'{i + 1} - Item: {random_item}')