# A module is a file containing python code such as variables, functions, classes and statements
# and can be used in another python programe

# python file ending with ``.py

# why do we need modules: code organization, avoid rewriting, reducing errors, Team development

# import calculator 
# import calculator import add, sub
# import calculator import *  (imports every function)

# print(calculator.add(10,20))
# print(calculator.sub(10,20))
# print(calculator.mul(10,20))
# print(calculator.div(10,20))

# Types of Modules- 
# Built-in/Standard Library Modules, these comes with python -eg -math, random, sys, os, datetime, statistics, calculator

# import math
# print(math.sqrt(25))

# User-defined - Modules created by yourself

# Third Party Modules:
# requests, django, flask, pandas, numpy
# these are developed outside python's standard library and arenormally installed seperately


# Module variable

# import calculator

# print(calculator.name)
# print(calculator.age)
# print(calculator.company)

# import math

# print(math.sqrt(25))
# print(math.pow(2, 3))
# print(math.ceil(4.2)) # round upwards
# print(math.floor(4.8)) # round downward
# print(math.factorial(5))
# print(math.pi)

# radius = 5
# area = math.pi * radius * radius
# print(area)

# import random
# number = random.randint(1, 10)
# print(number)
# names = ["C", "H", "E", "Y"]
# name = random.choice(names)
# print(name)
# nums = [1, 2, 3, 4, 5]
# random.shuffle(nums)
# print(nums)

# sys module

# import sys
# print(sys.version)

# sys.argv -  contains command line arguments

# import sys

# name = sys.argv[1]
# print("Helo", name)

# age= 15
# if age < 18:
#   print("Not eligible")
#   sys.exit() # Terminates the program
# print("eligible")

# Platform module- it is used to get info about computer 

# import platform

# #platform.system()- return os name
# print(platform.system())
# #platform.release()- OS release
# print(platform.release())
# print(platform.version())
# print(platform.machine()) # return machine architecture
# print(platform.processor())
# print(platform.python_version())
# print(platform.python_implementation())

# import platform
# if platform.system() == "Windows":
#   print("Running on Windows")
# elif platform.system() == "Linux":
#   print("Running on Linux")
# else:
#   print("Nothing")




