# try:
#   num = int(input("Enter number: "))
#   print("You entered: ", num)
# except ValueError:
#   print("Please enter valid no")

# try: code that may cause an error
# except: code to handle the error

# try:
#   a = int(input())
#   b = int(input())
#   result = a / b
#   print("Result: ", result)
# except ZeroDivisionError:
#   print("Cannot divide by zero")
# except ValueError:
#   print("Please enter numbers only")
# finally:
#   print("It will execute even if error occurs")

# try:
#   age = int(input("Enter age: "))
#   if age < 0:
#     raise ValueError("Age can't be negative")
#   print("Age: ", age)
# except ValueError as e:
#   print("Error: ", e)

# File Handling in python- it provides: create files, open files, read files, write files, 
# add, update, close


# student.txt

# Read()- reads full file
# file = open("student.txt", "r")
# data = file.read()
# print(data)
# file.close()

# Readline() - it read only one line
# file = open("student.txt", "r")
# data = file.readline()
# print(data)
# file.close()

# Readlines()- reads all lines and returns them as list
# file = open("student.txt", "r")
# data = file.readlines()
# print(data)
# file.close()

# Writing to a file

# file = open("student.txt", "w")
# file.write("Vikas\n")
# file.close()

# Append mode

# file = open("student.txt", "a")
# file.write("\nKiran")
# file.close()

# Difference:
# w - replace existing content
# a - add to existing content

# with open()- actomatically close our file, safe to use

# with open("student.txt", "r") as file:
#   data = file.read()
#   print(data)

# writing using withopen()
# with open("student.txt", "w") as file:
#   data = file.write("Rahul\n")
#   print(data)

# Reading line by line
# with open("student.txt", "r") as file:
#   for line in file:
#     print(line.strip())

# try:
#   with open("ABC.txt", "r") as file:
#     data = file.read()
#     print(data)
# except FileNotFoundError:
#   print("File does not exist")

# Real time Example: Student record
# name = input("Enter student name: ")
# age = input("Enter age: ")
# course = input("Enter course: ")

# with open("student.txt", "a") as file:
#   file.write(f"Name: {name}\n")
#   file.write(f"Age: {name}\n")
#   file.write(f"Course: {name}\n")
# print("Student details saved successfully.")

# balance  = 10000
# try:
#   amount = int(input("Enter withdraw amount: "))
#   if amount <= 0:
#     raise ValueError("Amount must be positive")
#   if amount > balance:
#     print("insufficient balance")
#   else:
#     balance -= amount
#     with open("tranaction.txt", "a") as file:
#       file.write(f"Withdrawn: {amount}\n")
#       file.write(f"Remaining balance: {balance}\n")
#     print("Success")
#     print("Remaining balance: ", balance)
# except ValueError as e:
#   print("Error: ", e)

