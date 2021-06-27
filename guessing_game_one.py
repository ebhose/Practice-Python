#!/usr/bin/env python3

import random


guess = input("Guess a number (exit to stop): ")

if guess == "exit":
    done = True
else:
    done = False


while not done:
    number = random.randrange(1, 10)

    if int(guess) < number:
        print("Your guess is too low")
        print(f"The number was {number}\n")
    elif int(guess) > number:
        print("Your guess is too high")
        print(f"The number was {number}\n")
    else:
        print("You guessed the number correctly")
        print(f"The number was {number}\n")

    guess = input("Guess a number (exit to stop): ")
    if guess == "exit":
        done = True
