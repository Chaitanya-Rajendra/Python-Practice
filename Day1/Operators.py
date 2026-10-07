#Operators is a symbol that tells the compiler to perform specific mathematical or logical manipulations.

# 10,20 - Operands
# + - Operator

# Types of Operators
# 1. Arithmetic Operators - these operators are used to perform mathematical operations like +, -, *, /, %, **, etc.
# Float / - decimal
# floor // - integer

a = 10
b = 3
print(a + b) #Addition
print(a - b) #Subtraction
print(a * b) #Multiplication
print(a / b) #Division
print(a // b) #Floor Division
print(a % b) #Modulus
print(a ** b) #Exponentiation


#2. Assignment Operators - these operators are used to assign values to variables.

a = 5
a += 3
print(a) # a = a + 3

#3. Comparison Operators - these operators are used to compare two values and return a boolean value (True or False).

# OR(+)  AND(*)  NOT(!)
# 0 0 0  0 0 0   0 1
# 0 1 1  0 1 0   1 0
# 1 0 1  1 0 0   1 0
# 1 1 1  1 1 1   0 1

#4. Logical Operators - these operators are used to combine conditional statements.

x = False
print(not x)

a = [1, 2, 3, 4, 5]
b = [4, 5, 6, 7, 8]
print(a is not b) # returns b if a is True


#is refers to check whether two names are belonging to the same object. 

#membership Operators - these operators are used to test whether a sequence is presented in an object.

a = [1, 2, 3, 4, 5]
print(3 in a) # returns True if 3 is in a
print(6 not in a) # returns True if 6 is not in a


#Identity operators - Is, is not

#Bitwise Operators - AND(&), OR(|), NOT(~) XOR(^), Left Shift(<<), Right Shift(>>)

#XOR(^) - returns 1 when both bits are different, otherwise returns 0.
#print(5 << 1) # returns 40 because 0101 << 1 = 1010

#Precedence of Operators - Bodmas - Brackets, Order, Division, Multiplication, Addition, Subtraction

#shopping program

price = 1000
quantity = 5
total = price * quantity
print(total)
if total >= 3000:
    discount = total * 0.10
    print("You are eligible for a discount of", discount)
else:
    discount = 0
    print("You are not eligible for a discount")
final_amount = total - discount
print("Final amount to be paid:", final_amount)


# less than 1000- no discount
# 1000-3000 - 10% discount
# 3000-8000-20
# 10000-30
# above 10000-50
# above 5000 - no delivery charges or 100 rs delivery

total = int(input())

if total < 1000:
    discount = 0
elif total <= 3000:
    discount = total * 0.1
elif total <= 8000:
    discount = total * 0.2
elif total <= 10000:
    discount = total * 0.3
else:
    discount = total * 0.5

if total > 5000:
    delivery_charge = 0
else:
    delivery_charge = 100

print("Discount:", discount)
print("Delivery charges:", delivery_charge)

final_amount = total - discount + delivery_charge

print("Final amount to be paid:", final_amount)


