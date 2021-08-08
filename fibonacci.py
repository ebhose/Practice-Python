#!/usr/bin/env python3


def fib(n):
    if n == 1:
        return 1
    if n == 2:
        return [1,1]

    fib = [1, 1]

    while n >= 3:
        new_fib = sum(fib[-2:])
        fib.append(new_fib)
        n -= 1
    return fib



if __name__ == '__main__':
    num = int(input("How many Fibonacci numbers would you like to generate: "))

    print(fib(num))
