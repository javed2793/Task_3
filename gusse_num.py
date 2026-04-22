import random

# store random number
number = random.randint(1, 10)

# take first guess
guess = int(input("Enter number between 1 to 10: "))

# loop until correct
while guess != number:
    if guess < number:
        print("Too low")
    else:
        print("Too high")

    guess = int(input("Try again: "))

print("Correct! You guessed it.")