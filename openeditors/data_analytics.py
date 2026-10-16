# Introduction to Data Analytics
# It is a process of collecting, cleaning, transforming, analyzing and interpreting data
# to find useful info and make decisions.

# Important Steps
#1. Data Collection:
# Excel, CSV, Database, APIs, Websites, Applications

#2. Data Cleaning
# missing values, Duplicate records, Incorrect Values, wrong formats

#3. data Processing
# converts the data into useful format.

#4. Data analysis
# Finding patterns and relationships

#5. Visualization:
# representing data using bar, line, pie, histograms

# Numpy= Numerical Python
# It is python library used for numerical calculations, working with arrays, mathematical
# operations, matrix operations.

# import numpy as np
# marks = np.array([80, 85, 90, 96])
# marks = marks + 5
# print(marks)


# 2D matrix
# import numpy as np

# marks = np.array([
#   [80, 90, 60],
#   [85, 95, 75],
#   [70, 80, 90]
# ])
# print(marks)
# print(marks.ndim)
# print(marks.shape)
# print(marks.size)
# print(marks.dtype)
# print(marks[0][0])
# print(marks[0][1])
# print(marks[0][2])
# print(marks[1][0])
# print(marks[1][1])
# print(marks[1][2])
# print(marks[2][0])
# print(marks[2][1])
# print(marks[2][2])
# print(marks[0:2, 1:3])
#[0:2] - row 0 and 1
#[1:3] - columns 1 and 2
#[0, 1] [0, 2] [1, 1] [1, 2]

# Creating Specil Arrays
#1. np.zeros()-  Creats an array filled with zeros.

# import numpy as np
# a = np.zeros(5)
# print(a)

#a = np.zeros((3, 4))
# print(a)

#2. np.ones()- it creats an array of ones
# import numpy as np
# a = np.ones((3,4))
# print(a)

# import numpy as np
# a = np.ones(5)
# print(a)

#3. np.arange()- it creats an array of evenly spaced values within a given range
# similar to  python range
# import numpy as np
# a = np.arange(1, 10)
# print(a)

# Array operations
# import numpy as np
# a = np.array([10, 20, 30])
# b = np.array([1, 2, 3])
# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)

#Comparision Operator
# import numpy as np
# a = np.array([10 , 20, 30, 40])
# print(a > 20)
# print(a[a > 20])

#Mathematical Functions

# marks = np.array([70, 75, 80, 85, 90])
# #Sum
# print(np.sum(marks))
# #Average
# print(np.mean(marks))
# #Maximum
# print(np.max(marks))
# #Minimum
# print(np.min(marks))

import numpy as np
# marks = np.array([
#   [80, 90, 60],
#   [85, 95, 75],
#   [70, 80, 90]
# ])
# #column wise
# print(np.sum(marks, axis = 0))
# #Row wise
# print(np.sum(marks, axis = 1))

#Reshaping array

a =np.array([1, 2, 3, 4, 5, 6])
b = a.reshape(2, 3)
print(b)
