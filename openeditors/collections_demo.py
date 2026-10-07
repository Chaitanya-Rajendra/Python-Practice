# collections- specialized data structures eg: List, Tuple, Set, dictionary

# import collections #- default dict, counter, deque, named tuple

# Counter- Counter is used to count how many times item occurs.
# from collections import Counter

# from collections import Counter
# nums = [1, 1, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4]
# # text = "banana"
# count = Counter(nums)
# print(count)

# Default Dict- It allows us to provide default value

# from collections import defaultdict
# students = defaultdict(int)
# print(students["Python"])

# Grouping students based on their batch
# from collections import defaultdict
# students = defaultdict(list)
# students["CSE"].append("Rahul")
# students["CSE"].append("S")
# students["ECE"].append("Y")
# print(students)

# Deque- double ended queue- 

# from collections import deque

# nums = deque([10, 20, 30])

# nums.append(40)
# print(nums)

## add at begining
# nums.appendleft(5)
# print(nums)

## Delete from last
# POP()- Delete from last
# nums.pop()
# print(nums)

#Delete from Begining
# nums.popleft()
# print(nums)

# Named Tuple- A named tuple is like a tuple whose values can also be accessed by using name

# student = ("Rahul", 20, "CSE")
# print(student[0])

# from collections import namedtuple

# Student = namedtuple("Student", ["name", "age", "branch"])
# student = Student("Rahul", 20, "CSE")
# print(student.name)
# print(student.age)
# print(student.branch)

# Itertools- It provides tools to work with Iterators
# import itertools

# combinations, permutations, Cartesian product, Grouping

# 1).count()
# import itertools
# numbers = itertools.count(1)
# print(next(numbers))
# print(next(numbers))
# print(next(numbers))

# 2).cycle()- repeats elements again and again
# import itertools
# colors = itertools.cycle(["Red", "Green", "Blue"])
# print(next(colors))
# print(next(colors))
# print(next(colors))
# print(next(colors))
# print(next(colors))

# 3). Permutations()- it represents different arguments/ orders
# from itertools import permutations
# nums = [1, 2, 3]
# result = permutations(nums)
# for item in result:
#   print(item)

# 4). Combinations()- it selects items where order doesn't matter
# from itertools import combinations
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# result = combinations(nums, 2)
# for item in result:
#   print(item)

# 5). chain()- combines multiple iterables into one sequence.
# from itertools import chain
# a = [1, 2, 3]
# b = [4, 5, 6]
# result = chain(a, b)
# for x in result:
#   print(x)

# 6). Datetime module- date, time, date + time, time differnces, formatting
# from datetime import date
# today = date.today()
# print(today)
# print(today.year)
# print(today.month)

# from datetime import datetime
# now = datetime.now()
# print(now)

# from datetime import date
# birthday = date(2004, 11, 23)
# print(birthday)

# Creating specific Date and Time
# from datetime import datetime
# dt = datetime(2026, 9, 24, 15, 30)
# print(dt)

# Timedelta - Represents difference between dates / times
# from datetime import date, timedelta
# today = date.today()
# future = today + timedelta(days = 10)
# print(today)
# print(future)

# Date difference
# from datetime import date
# date1 = date(2004, 11, 23)
# date2 =date(2026, 9, 26)
# diff = date2 - date1
# print(diff)
# print(diff.days)

# Formatting Date- strftimme()
# from datetime import datetime
# now = datetime.now()
# formatted = now.strftime("%d-%m-%Y")
# print(formatted)

# from datetime import datetime
# date_string = "26-09-2026"
# date_object = datetime.strptime(date_string, "%d-%m-%Y")
# print(date_object)

