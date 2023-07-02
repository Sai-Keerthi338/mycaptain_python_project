# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 01:31:08 2023

@author: Dell
"""

def print_positive_numbers(numbers):
    positive_numbers = []
    for num in numbers:
        if num > 0:
            positive_numbers.append(num)
    print("Output:", positive_numbers)

list1=input("list1 :")

print_positive_numbers(list1)

list2 = input("list2 :")

print_positive_numbers(list2)