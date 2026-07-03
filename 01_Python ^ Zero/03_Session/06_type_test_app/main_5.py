import time
import random

file = open('sentences.txt', 'r')
sentences = file.readlines()
file.close()

print("Get ready to start quiz 📣")
input('Press any key to start...')

random_sentence = random.choice(sentences)

print(random_sentence)

time_1 = time.time()

user_text = input('Enter a sentence: ')

time_2 = time.time()

total_time = time_2 - time_1

print(f"time: {total_time:.2f} seconds")

random_words = random_sentence.split()
user_words = user_text.split()

corrects, incorrects = 0, 0

for idx in range(len(random_words)):
    if idx < len(user_words):
        if random_words[idx] == user_words[idx]:
            corrects += 1
            print(f"\033[32m{random_words[idx]}", end=" ")
            continue

    incorrects += 1
    print(f"\033[31m{random_words[idx].upper()}", end=" ")

print('\033[97m')

print(f"corrects: {corrects}, incorrects: {incorrects}")
print(f"Speed type: {corrects / total_time:.2f} word of seconds")