# scope- scope is the region of a program where a variable can be accessed

# 1). local scope
# 2). global scope

# Local scope- A variable created inside a function 

# def display():
#   name = "chaitu"
#   age = 21
#   print(name)
#   print(age)

# display()

#Diff functions can have variables with same name

# def first():
#   x = 10
#   print(x)

# def second():
#   y = 20
#   print(y)

# first()
# second()

#global scope- A variable created outside a function 

# name = "chaitu"
# age = 21

# def display():
#   print(name)
#   print(age)
# display()
# print(name)

# name = "chaitu"
# age = 21

# def display():
#   name = "bob"
#   print(name)
#   print(age)
# display()
# print(name)

# x = 100

# def display():
#   global x
#   x = 200
# print(x)
# display()
# print(x)

#pass by value and pass by reference

# def display(x):
#   print(x)
# a = 10
# display(a)

# def display(x):
#   x = 20
# a = 1
# display(a)
# print(a)

#pass by value- copy of value changes, orginal remains same, changes made inside the value doesn't change

# def change(x):
#   x = 20
#   print("Inside func: ", x)
# a = 10
# change(a)
# print("outside func: ", a)

#a -> 10
#Calling the func changes(a)
#X receives a reference to the same integer object
#x = 20
#before:
#a -> 10 x = 10
#after x = 20
#a - 10, x = 20

# def add_10(x):
#   x += 10
#   print("inside func: ", x)
# nums = 50
# add_10(nums)
# print("outside func: ", nums)

#pass by reference - copy of value changes, orginal values also changes

# def add_element(data):
#   data.append(40)
# values = [10, 20, 30]
# add_element(values)
# print(values)

#recursion - function calling itself

#in for loop
# for i in range(5, 0 , -1):
#   print(i)

# def count_down(n):

#   #base case
#   if n == 0:
#     return

#   #recursion case
#   print(n)
#   count_down(n-1)

# count_down(5)

#Factorial of a number using recursion

# def fact(n):
#   #base case
#   if n <= 1:
#     return 1

#   #recursive case
#   return n * fact(n-1)
# print(fact(5))

# def fib(n, first=1, second=1):
#   if n == 0:
#     return

#   print(first, end=" ")
#   fib(n - 1, second, first + second)

# fib(6)


