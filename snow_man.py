import random

words = []

with open("words.txt", "r") as f:
    words = f.read().split()

index = random.randint(0, len(words) - 1)

random_word = words[index]



