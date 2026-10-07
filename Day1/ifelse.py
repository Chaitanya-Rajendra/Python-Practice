#conditional statements

#executes or works based on condition

#if, elif, else
#1. if statement
#if means execute the code only when condition is True

#age = 18
#if age < 20:
#  print("Eligible")

#age = int(input())
#if age >= 21:
#  print("alcohol permitted")
#else:
#  print("alcohol not permitted")

#marks =  int(input())
#if marks >= 90:
#  print("A+")
#elif marks >= 80:
#  print("A")
#elif marks >= 70:
#  print("B")
#elif marks >= 60:
#  print("C")
#elif marks >= 50:
#  print("D")
#elif marks >= 40:
#  print("E")
#else:
#  print("F")

#1. real time example - Atm
#is the card valid?
#is this pin correct?
#is there enough balance?
#withdraw

'''
card = input("Is your card valid? ")

if card == "yes":
    print("Card is valid")
else:
    print("Card is invalid")
    exit()

pin = int(input("Enter your PIN: "))

if 1000 <= pin <= 9999:
    print("PIN is valid")
else:
    print("Only 4-digit numbers are allowed")
    exit()

balance = 60000

if balance > 0:
    print("There is enough balance")
else:
    print("Insufficient balance")
    exit()

withdraw = int(input("Enter withdrawal amount: "))

if withdraw <= balance:
    print("Withdrawal successful")
    balance = balance - withdraw
    print("Remaining balance:", balance)
else:
    print("Insufficient balance")
'''

#2.online shopping
#is the product available?
#login with account
#is payment done?


login = input("Do you want to login? ")

if login == "yes":
    login = input("enter your mail id: ")
    print("Login successful")
else:
    print("Please login to continue")
    exit()

product = input("enter the product: " )

if product in ["phone", "Laptop", "Charger", "IPad", "Macbook"]:
  print("available")
else:
  print("Product is not available")


