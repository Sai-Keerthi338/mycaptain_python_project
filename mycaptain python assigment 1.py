# -*- coding: utf-8 -*-
"""
Created on Sat Jul  1 17:30:06 2023

@author: Dell
"""

#question 1
import math


radius=float(input("the radius of the circle : "))
area=math.pi*radius**2

print (" The area of the circle with radius",radius,"is:",area)


#question 2


extension_to_language = {
    "py": "Python",
    "java": "Java",
    "cpp": "C++",
    "txt": "Plain Text",
    "html": "HTML",
    "css": "CSS",
    "js": "JavaScript",
    
    }
filename=input("Input the filename: ")



extension=filename.split(".")[-1]

language=extension_to_language.get(extension)


print("Extension of the file is:",language)
