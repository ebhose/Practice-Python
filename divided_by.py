#!/usr/bin/env python3


num = int(input("Enter a number: "))
check = int(input("Enter a second number: "))

if num % check == 0:
    print(f"{num} is evenly divisible by {check}")
else:
    print(f"{num} is not divisible by {check}")
