#!/usr/bin/env python3

import datetime

name = input("Enter your name: ")
age = int(input("Enter your age: "))
repeat = int(input("How many times you want the message repeated?: "))

year = datetime.datetime.now().year

print()
for times in range(repeat):
    print(f"{name} you will be 100 years old in the year {year + 100 - age}.")

