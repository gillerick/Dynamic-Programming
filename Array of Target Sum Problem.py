def howSum(targetSum, numbers):
    T = []
    if targetSum == 0:
        return []
    if targetSum < 0:
        return None
    for num in numbers:
        remainder = targetSum - num
        remainderResult = howSum(remainder, numbers)
        if remainderResult != None:
            # Spread operator in Python
            T = [*remainderResult, num]
            return T
    return None


print(howSum(7, [2, 3]))
print(howSum(7, [5, 4, 3, 7]))
