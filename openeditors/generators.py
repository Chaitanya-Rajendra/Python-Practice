# numbers= []
# for i in range(1, 6):
#   numbers.append(i)
# print(numbers)

# numbers = [i for i in range(1, 6)]
# print(numbers)
#one line representaion of loop
#Syntax: [expression for variable in iterable]
#[x for x in range(1, 5)]

# squares = [i * i for i in range(1, 6)]
# print(squares)

# names = ["sam", "ram", "jam"]
# result = [name.upper() for name in names]
# print(result)

# numbers = []
# for i in range(1, 11):
#   if i % 2 ==0:
#     numbers.append(i)
# print(numbers)

# numbers = [i for i in range(1, 11) if i % 2 == 0]
# print(numbers)

#filtering values
# nums = [10, 12, 20, 25, 30, 35, 40]
# result = [i for i in nums if i > 20]
# print(result)

#nested list comprehension- it means having more than one for loop inside list comprehension

# result = []
# for i in range(1, 4):
#   for j in range(1, 4):
#     result.append((i, j))
# print(result)

# result = [(i, j) for i in range(1, 4) for j in range(1, 4)]
# print(result)

# matrix = [
#   [1, 2, 3],
#   [4, 5, 6],
#   [7, 8, 9]
# ]
# result = [x for row in matrix for x in row]
# print(result)

#Generators- Generators produce value one at a time when required

# def numbers():
#   for i in range(1, 6):
#     yield i
# result = numbers()
# print(result)

#yield passes the function and remember it's current state

# def numbers():
#   yield 1
#   yield 2
#   yield 3
# result = numbers()
# print(next(result))
# print(next(result))
# print(next(result))

# def numbers2():
#   for i in range(1, 6):
#     yield i
# result = numbers2()
# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result))

# def numbers():
#   yield 1
#   yield 2
#   yield 3
# result2 = numbers()
# print(next(result2))
# print(next(result2))
# print(next(result2))

# yield vs return
# def demo():
#   return 10
#   return 20
# print(demo())

# def demo():
#   yield 10
#   yield 20
#   yield 30
# result = demo()
# print(next(result))
# print(next(result))
# print(next(result))

#understanding generator execution

# def demo():
#   print("start")
#   yield 10
#   print("middle")
#   yield 20
#   print("end")
#   yield 30
# result = demo()
# print(next(result))
# print(next(result))
# print(next(result))

#using generator with for loop

# def numbers():
#   for i in range(1,6):
#     yield i
# for x in numbers():
#   print(x)

#Generator expression

#List Comp = []
#Generator Exp = ()

# nums = (x * x for x in range(1, 6))
# print(next(nums))
# print(next(nums))
# print(next(nums))
# print(next(nums))
# print(next(nums))

# we need to use generators when we want to generate values at a time

#create a generator that produces even no.s from 1 to 20

# def even():
#   for i in range(1, 21):
#     if i % 2 == 0:
#       yield i
# for x in even():
#   print(x)



