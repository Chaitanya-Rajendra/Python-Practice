# #function_creation or definition
# def greet(): #greet() - function name
#   #function body
#   return "Hello Students"
# #function_calling
# print(greet())

#user-defined function

#type -1 no parameters, no return value
# def greet():
#     print("Hello Students")
# greet()

#type -2 parameters, no return value
# def greet(name):
#   print("Hello", name)
# greet("Vikas")

#type -3 no parameters, but return value
# def get_number():
#   return 100
# result = get_number()
# print(result)

#type -4  parameters, return value
# def add(a, b): #a, b are parameters
#   return a + b
# print(add(2, 3)) #2, 3 are arguments

#result - gives the result back to the program

# def calc(a, b):
#   add = a + b
#   sub = a - b
#   return add, sub
# x, y = calc(20, 10)
# print(x)
# print(y)

#Positional Arguments
#Arguments are matched based on their position
#order is important

# def student(name, age):
#   print("Name: ", name)
#   print("Age: ", age)
# #functional_calling
# student("chaitu", 21)

#keyword arguments

# def student(name, age):
#   print(name)
#   print(age)
# student(age=25, name= "Chaitu")

#default arguments

# def greet(name = "student"):
#   print("Hello", name)
# greet() # greet("ME")

#variable- length arguments (*args)

# def add(a, b):
#   print(a + b)
# add(2, 3, 4, 5, 6, 7, 8)

# def add(*numbers):
#   total = 0
#   for number in numbers:
#     total += number
#   return total
# print(add(10, 20))
# print(add(1, 2, 3, 4, 5, 6, 7, 8, 9))

#*args- it collects multiple arguments into a tuple

#keyword variable-length arguments(**kwargs)

#accepts multiple keyword argumets

# def student_details(**details):
#   print(details)
# student_details(
#   name = "chaitu",
#   age = 21,
#   city = "Hyd"
# )

#**kwargs -> dictionary

# def example(*args,**kwargs):
#   print(args)
#   print(kwargs)
# example(10, 20, 30, name = "chaitu", age = 21)


