# with open('text.txt', 'r', encoding='utf-8') as file:
#     text = file.readlines()
#
# print(text)

text = input('Enter your text: ')

with open('text.txt', 'a', encoding='utf-8') as file:
    file.write(text)