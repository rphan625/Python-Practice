""" Exercise 9
    Guessing Game One
    Generate random number, guess number, notify if low, high or right
    Extras:
        Keep game going until user types 'exit'
        Keep track of how many guesses, print when game ends
"""

import random

randNum = random.randint(1, 9)

guessCount = 0
gameRunning = True

while gameRunning:
    guess = input("Guess a number between 1-9: ")
    if guess == "exit":
        gameRunning = False
    elif int(guess) == randNum:
        print("Correct Guess!")
        guessCount += 1
        randNum = random.randint(1, 9)
        print("Changing number!")
    elif int(guess) > randNum:
        print("Too High!")
        guessCount += 1
    else:
        print("Too Low!")
        guessCount += 1

print("Game Over!")
print(f"Number of Guess: {guessCount}")
