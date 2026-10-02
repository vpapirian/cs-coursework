import random

number = random.randint(0, 1000)

guesses = 0

while True:
    guess = int(input("Guess the number (0-1000): "))
    guesses += 1

    if guess < number:
        print("Guess higher")
    elif guess > number:
        print("Guess lower")
    else:
        print(f"It took {guesses} guesses to get to the right number")
        break