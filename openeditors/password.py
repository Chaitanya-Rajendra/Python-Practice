# Random password Generator

# import random 

# characters = "!@#$%&*()+-^abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
# password = ""
# for i in range(8):
#   password += random.choice(characters)
# print("password: ", password)

# password generator using string

# import random
# import string

# characters = string.ascii_letters + string.digits + string.punctuation
# password = ""
# for i in range(8):
#   password += random.choice(characters)
# print("password: ", password)

# ATM examples: if, else, elif, variables, input, arthemetic operations, logical thinking

# check pin

# correct_pin = 1234

# pin = int(input("enter pin: "))
# if pin == correct_pin:
#   print("access granted")
# else:
#   print("Invalid PIN")

# Add balance

# balance = 10000
# deposit = 5000
# pin = int(input("Enter PIN: "))
# if pin == 1234:
#   print("access granted")
#   balance += deposit
#   print(balance)
# else:
#   print("Invalid PIN")

# Withdraw

# balance = 10000

# pin = int(input("Enter PIN: "))
# if pin == 1234:
#   amount = int(input("Enter withdraw amount: "))
#   if amount <= balance:
#     balance -= amount
#     print("withdraw successful")
#     print("Remaining balance: ",balance)
#   else:
#     print("Insufficient Balance")
# else:
#   print("Invalid PIN")

# Complete ATM example

# balance = 10000
# pin = int(input("Enter PIN: "))
# if pin == 1234:
#   print("\n1.Check Balance")
#   print("2. Withdraw")
#   print("3. Deposit")
#   choice = int(input("Enter your choice: "))
#   if choice == 1:
#     print("balance: ", balance)
#   elif choice == 2:
#     amount = int(input("Enter withdraw amount: "))
#     if amount <= balance:
#       balance -= amount
#       print("withdraw Successful")
#       print("remaining balance", balance)
#     else:
#       print("Insufficeint balance")
#   elif choice == 3:
#     amount = int(input("Enter Deposit amount: "))
#     balance += amount
#     print("Deposit successful")
#     print("Updated balance", balance)
#   else:
#     print("Invalid choice")
# else:
#   print("Invalid PIN")


