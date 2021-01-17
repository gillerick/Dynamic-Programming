"""
Write a function 'bestSum(targetSum, numbers)' that takes in a targetSum and an array of numbers as arguments.
The function should return an array containing the shortest combination of numbers that add up to exactly the targetSum.
If there is a tie for the shortest combination, you may return any one of the shortest.

"""

def bestSum(targetSum, numbers):
    T = []
    if targetSum == 0:
        return []
    if targetSum < 0:
        return None

    shortestCombination = None
    for num in numbers:
        remainder = targetSum - num
        remainderCombination = bestSum(remainder, numbers)
        if remainderCombination != None:
            T = [*remainderCombination, num]
    #         If the combination is shorter than the current "shortest", update it
            if shortestCombination == None or len(T) < len(shortestCombination):
                shortestCombination = T

    return shortestCombination


print(bestSum(7, [5, 3, 4, 7]))
print(bestSum(8, [2, 3, 5]))
print(bestSum(100, (2, 1, 4, 25)))
