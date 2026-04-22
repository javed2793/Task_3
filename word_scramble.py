import random

# list of words
words = ['python', 'java', 'guvi', 'selenium']

# choose a word
word = random.choice(words)

# convert word into list
letters = list(word)

# shuffle letters
random.shuffle(letters)

# join letters to make scrambled word
scrambled = ""
for ch in letters:
    scrambled = scrambled + ch

print("Guess the word:", scrambled)

# give 3 chances
for i in range(3):
    guess = input("Enter your answer: ")

    if guess == word:
        print("Correct!")
        break
    else:
        print("Wrong, try again")

# if not guessed
if guess != word:
    print("Game Over! Word was:", word)