# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 01:18:24 2023

@author: Dell
"""



def fibonacci(n):
    if n <= 1:
        return n

    fib_0 = 0
    fib_1 = 1

    for _ in range(2, n + 1):
        fib = fib_0 + fib_1
        fib_0 = fib_1
        fib_1 = fib

    return fib

n = int(input("Enter the number of Fibonacci numbers to generate: "))

fib_sequence = []
for i in range(n):
    fib_sequence.append(fibonacci(i))
print("Fibonacci sequence:", fib_sequence)













