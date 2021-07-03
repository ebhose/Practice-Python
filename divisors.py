#!/usr/bin/env python3

import math
import time

num = int(input("Enter a number: "))


dividend = math.floor(math.sqrt(num))

def divisor(num, dividend):
    divisorList = []

    for divisor in range(1, dividend + 1):
        quotient = num // divisor
        if num % divisor == 0:
            divisorList.extend((divisor, quotient))

    #return sorted(list(set(divisorList)))
    return set(divisorList)


def divisor2(num):
    listRange = list(range(1,num+1))

    divisorList = []

    for number in listRange:
        if num % number == 0:
            divisorList.append(number)

    return divisorList



start = time.time_ns()
divisor(num, dividend)
stop = time.time_ns()

print(f"Function divisor took {(stop - start) // 1000} msec to complete")

start = time.time_ns()
divisor2(num)
stop = time.time_ns()

print(f"Function divisor2 took {(stop - start) // 1000} msec to complete")


#print(divisorList)
#print(divisorList2)

#print(divisorList == divisorList2)

