def howSum(targetSum, numbers, memo={}):
    if targetSum in memo:
        return targetSum[memo]
    if targetSum == 0:
        return []
    if targetSum < 0:
        return None
    for num in numbers:
        remainder = targetSum - num
        if howSum(remainder, numbers, memo):
            memo[targetSum] = True
            return True
        # if remainderResult != None:
        #     T = [*remainderResult, num]
    return False



print(howSum(7, [2, 3]))
print(howSum(7, [5, 4, 3, 7]))
