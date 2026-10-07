#lambda functions

#Anonymous- without name
#Small functions
#Single line functions

#lambda syntax:
#lambda arguments : expression

# def square(x):
#   print(x*x)
# square(5)

#lambda:
#lambda with one parameter
# square = lambda x : x * x
# print(square(6))

#lambda with multiple parameters
# add = lambda x, y : x + y
# print(add(10,20))

#lambda with if-else
# check = lambda x: "Even" if x % 2 == 0 else "Odd"
# print(check(7))
# print(check(10))

#when should we use lambda? - small functions for temporarily, especially with:
#map(), filter(), sorted(), reduce()

#map()- it applies function to every element, of an iterable
#Syntax: map(function, iterable)
# nums = [1, 2, 3, 4, 5]
# squares = list(map(lambda x : x * x, nums))
# print(squares)

#map without lambda

# def square(x):
#   return x * x

# numbers = [1, 2, 3, 4, 5]
# result = map(square, numbers)
# print(list(result))

#filter() - it is used when we want to select only element that satisfy a condition
#Syntax: filter(function, iteraction)

# nums = [1, 2, 3, 4, 5,6]
# result = filter(lambda x: x % 2 == 0, nums)
# print(list(result))

#reduce()- it repeatedly applies a function to elements and reduces entire sequence to one final value

#from functools import reduce
# from functools import reduce

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# result = reduce(lambda a, b : a + b, numbers)
# print(result)

# numbers = [1, 2, 3, 4]
# result = reduce(lambda a, b : a * b, numbers)
# print(result)

# nums = [10, 20, 30, 40]
# result = sorted(nums, reverse=True)
# print(result)

# names = ["chey", "bob", "bobby", "venky", "sai"]
# result = sorted(names, key=len)
# print(result)

#sorting numbers according to absolute values

# nums = [-10, -8, 2, 7, -13, 21]
# result = sorted(nums,key=abs)
# print(result)

#sorting number by last character
# names = ["chey", "bob", "bobby", "venky", "sai"]
# result = sorted(names, key=lambda x : x[-1])
# print(result)

#Sorting Tuple by marks

# students = [
#   ("r", 85),
#   ("v", 80),
#   ("p", 78),
#   ("s", 100)
# ]
# result = sorted(students, key=lambda x : x[1])
# print(result)





