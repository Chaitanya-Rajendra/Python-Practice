# for i in range(1,6):
#   for j in range(1, i + 1):
#     print(j, end="")
#   print()

# for i in range(1,6):
#   for j in range(1, i + 1):
#     print(i, end="")
#   print()

# for i in range(1, 6):
#   for j in range(5, 5 - i, - 1):
#     print(j, end="")
#   print()

# num = 1
# for i in range(1, 5):
#     for j in range(i):
#         print(num, end="")
#         num += 1
#     print()

# for i in range(5):
#   for j in range(5, 0, -1):
#     print(j, end="")
#   print()

# for i in range(5,0,-1):
#   for j in range(5, 5-i, -1):
#     print(j, end="")
#   print()

# for i in range(1,6):
#   for j in range(i, 0, -1):
#     print(j, end="")
#   print()


# Pyramid pattern

# n = 5
# for i in range(1, n + 1):
#     for j in range(n - i):
#         print(" ",end="")

#     for j in range(1, 2*i):
#         print(j, end = "")
#     print()

# n = 5
# for i in range(1, n + 1):
#     for j in range(n - i):
#         print(" ",end="")

#     for j in range(1, 2*i):
#         print(i, end = "")
#     print()

# n = 5
# for i in range(5, 0, -1):
#     for j in range(n - i):
#         print(" ",end="")

#     for j in range(1, 2*i):
#         print("*", end = "")
#     print()

# n = 5
# for i in range(1,n + 1):
#   for j in range(n-i):
#     print(" ", end = "")
#   for j in range(1, 2*i):
#     print("*", end ="")
#   print()
# lower body
# for i in range(n-1, 0, -1):
#   for j  in range(n-i):
#     print(" ", end="")
#   for j in range(1, 2*i):
#     print("*", end="")
#   print()

#Name pattern

# name = "CODE"
# for i in range(len(name)):
#   for j in range(i + 1):
#     print(name[j], end="")
#   print()

# name = "CODE"
# for i in range(len(name)):
#   for j in range(i + 1):
#     print(name[0], end="")
#   print()

# name = "CODE"
# for i in range(len(name)):
#   for j in range(i + 1):
#     print(name[i], end="")
#   print()


# n = 5
# for i in range(1,n + 1):
#   for j in range(n-i):
#     print(" ", end = "")
#   for j in range(1, 2*i):
#     if i == n:
#       print("*", end="")
#     elif j == 1 or j ==2 * i - 1:
#       print("*", end="")
#     else:
#       print(" ", end="")
#   print()

