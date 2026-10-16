#2. binary search- 
# Linear search- It search elements one by one(sequential)
# -It works on sorted and unsorted array.

# best - O(1)
# average - O(N)
# Worst - 

#Searching Algorithm

# def linear_search(arr, target):
#   for i in range(len(arr)):
#     if arr[i]==target:
#       return i
#   return -1
# arr = [10, 20, 30, 40]
# target= 20
# result = linear_search(arr, target)
# if result != -1:
#   print("Element found at index: ", result)
# else:
#   print("element not found")

# Binary search- Divide and Conquer

def binary_search(arr, target):
  left = 0
  right = len(arr)-1
  while left <= right:
    mid = left + right // 2
    if arr[mid] == target:
      return mid
    elif arr[mid] < target:
      left = mid + 1
    else:
      right = mid - 1
  return -1
arr = [10, 20, 30, 40, 50]
target= 20
result = binary_search(arr, target)
if result != -1:
  print("Element found at index: ", result)
else:
  print("element not found")

