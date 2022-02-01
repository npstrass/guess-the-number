# number guessing game where the user determines the range and then guesses a number
# programmed to indicate if guess is too high or too low
# give it a try and have fun! All suggestions are appreciated :)

import random

range_input = int(input("Give me a random number: "))


def guess(x):
    computer = random.randint(1, x)
    user = 0
    while user != computer:
        user = int(input(f"Now, guess a number between 1 and {x}: "))
        if user > computer:
            print("Just a bit too high! Try again..")
        elif user < computer:
            print("Not high enough! Give it another go..")

    print(f"YOU DID IT! The number was {computer}")


guess(range_input)
