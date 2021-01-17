"""
Write a function canSum(targetSum, numbers) that takes in a targetSum and an array of numbers as arguments.
The function should return a boolean indicating whether or not it is possible to generate the targetSum using numbers
from the array.

You may use an element as many times as needed.

Assume that all input numbers are non-negative.

"""
def canSum(targetSum, numbers):
    if targetSum < 0:
        return False
    if targetSum == 0:
        return True
    for num in numbers:
        remainder = targetSum - num
        if canSum(remainder, numbers):
            return True
    return False


print(canSum(7, [2, 3]))
print(canSum(8, [2, 3, 5]))
print(canSum(300, [7, 14]))
