#indentify number either +ve or -ve or zero

#n = int(input("enter number: "))
#if n > 0:
#  print("positive")
#elif n < 0:
#  print("negative")
#else:
#  print("zero")

#n = int(input("enter number: "))
#if n % 2 == 0:
#  print("even")
#elif n % 2 != 0:
#  print("odd")
#else:
#  print("zero")

#3. Largest of two numbers

# a = int(input("enter first no: "))#b = int(input("enter second no: "))
# if a > b:
#   print("first number is larger")
# elif b > a:
#   print("second number is larger")
# else:
#   print("both are equal")

#4. college adminstration

# marks = int(input("enter marks: "))
# entrance = input("did you pass entrance exam? (yes,no): ")

# if marks >= 60 and entrance == "yes":
#   print("eligible")
# else:
#   print("not eligible")

#5. login system

# username = input("enter user name: ")
# password = input("enter user name: ")
# if username == "admin" and password == "password123":
#   print("logged in")
# else:
#   print("incorrect details")

#6. driving eligibility

#age is 18 above
#derivinglicence
#under 18 - too young to drive
#18+ but no licence - valid licence required
#18 with licence - you can drive

# age = int(input("enter your age: "))

# if age >= 18:
#   license_valid = input("valid licence(yes/no): ")
#   if license_valid == "yes":
#     print("you can drive")
#   else:
#     print("valid licence required")
# else:
#   print("too young to drive")


# movie ticket price
# below 5 - free
# 5 - 12 - 100
# 13 - 59 -200
# 60 and above - 120

# age = int(input("enter your age: "))
# if (age < 5):
#   print("free ticket")
# elif (age < 12):
#   print("ticket price is 100")
# elif (age < 59):
#   print("ticket price is 200")
# else:
#   print("ticket price is 120")

# 7.leap year

# year = int(input("enter year: "))

# if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
#   print("its a leap year")
# else:
#   print("its not a leap year")

#employe management system
#performance > 90 and exp > 5 = 20% hike
#performance > 90 and exp < 5 = 15% hike
#performance > 80 = 10% hike
#performance > 70 = 5% hike

# salary = int(input("enter your salary: "))
# performance = int(input("performance: "))
# experience = int(input("enter years of experience: "))

# if performance >= 90 and experience >= 5:
#   hike = salary * 0.2
#   final_salary = salary + hike
#   print("20% hike")

# elif performance >= 90 and experience < 5:
#   hike = salary * 0.15
#   final_salary = salary + hike
#   print("15% hike")

# elif performance >= 80:
#   hike = salary * 0.1
#   final_salary = salary + hike
#   print("10% hike")

# else:
#   hike = salary * 0.05
#   final_salary = salary + hike
#   print("5% hike")

# print(final_salary)


#palindrome number

#eg: 121, 12321,

# num = int(input("enter a num: "))
# orginal = num
# reverse = 0

# while num > 0:
#   digit = num % 10
#   reverse = reverse * 10 + digit
#   num //= 10

# if orginal == reverse:
#   print("Palindrome")
# else:
#   print("Not a palindrome")

#Factorial

#5! = 5 * 4 * 3 * 2 * 1 = 120

# num = int(input("enter a num: "))
# factorial = 1

# while num > 0:
#   factorial *= num
#   num -= 1
# print(factorial)

#fibonacci - 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55

# num = int(input("enter a num: "))
# a = 0
# b = 1

# for i in range(num):
#   print(a, end=" ")
#   a, b = b, a + b


#Finding Duplicate numbers in a list

# numbers = [1, 2, 3, 4, 5, 2, 6, 4, 7, 8]
# for i in range(len(numbers)):
#   for j in range(i+1, len(numbers)):
#     if numbers[i] == numbers[j]:
#       print(numbers[i])

