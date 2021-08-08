#!/usr/bin/env python3


import divisors
import math


def isPrime(num):
    if num < 2:
        return False
    elif num % 2 == 0 and num != 2:
        return False
    elif len(divisors.divisor2(num)) == 2:
        return True
    else:
        return False


def isPrime2(num):
    if num < 2:
        return False
    elif num % 2 == 0 and num != 2:
        return False

    for n in range(2, math.ceil(math.sqrt(num))):
        if num % n == 0:
            print(n)
            return False
    return True


if __name__ == '__main__':
    num = int(input("Enter a number: "))

    if isPrime2(num):
        print(f"{num} is a prime number")
    else:
        print(f"{num} is not a prime number")
