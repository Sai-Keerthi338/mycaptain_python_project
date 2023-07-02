# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 01:51:56 2023

@author: Dell
"""

def most_frequent(string):
    freq_dict = {}

    for letter in string:
        if letter in freq_dict:
            freq_dict[letter] += 1
        else:
            freq_dict[letter] = 1

    sorted_freq = sorted(freq_dict.items(), key=lambda x: x[1], reverse=True)

    for item in sorted_freq:
        print(f"{item[0]} = {item[1]:02d}")

input_string = input("Please enter a string: ")

most_frequent(input_string)
