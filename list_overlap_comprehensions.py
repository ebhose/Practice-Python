#!/usr/bin/env python3

import random

# Generate 15 random numbers between 1 and 80
a = sorted(random.sample(range(60), 15))
b = sorted(random.sample(range(60), 12))

print(a)
print(b)

temp = [item for item in a if item in b]

result =[]

for item in temp:
    if item not in result:
        result.append(item)


print(result)

