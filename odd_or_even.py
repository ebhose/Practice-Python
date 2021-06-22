#!/usr/bin/env python3

number = int(input("Enter a number: "))

def odd_or_even(number):
    if number % 2 == 0 and number % 4 == 0:
        print(f"{number} is an even number and divisible by 4.")
    elif number % 2 == 0:
        print(f"{number} is an even number.")
    else:
        print(f"{number} is an odd number.")


odd_or_even(number)
