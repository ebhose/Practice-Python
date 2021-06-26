#!/usr/bin/env python3


number = int(input("Enter a number: "))

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

new_list = [ item for item in a if item < number]

print(new_list)


