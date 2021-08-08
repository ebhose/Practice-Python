#!/usr/bin/env python3


import sys
import primality as prime
import fibonacci as fibo


num = int(sys.argv[1])

fib_series = fibo.fib(num)

fib_prime = [item for item in fib_series if prime.isPrime2(item)]

print(fib_prime)
