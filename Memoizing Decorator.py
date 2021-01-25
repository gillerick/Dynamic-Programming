from functools import wraps

def memo(func):
    cache = {}
    @wraps(func)
    def wrap(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrap
@memo
def fib(i):
    if i < 2:
        return 1
    else:
        return fib(i-1) + fib(i-2)

# print(fib(1))
# print(fib(5))
# print(fib(10))
# print(fib(100))


def targetSum(target, nums):
    if target < 0:
        return False
    if target == 0:
        return True
    for num in nums:
        remainder = target - num
        if targetSum(remainder, nums):
            return True
    return False

print(targetSum(8, [2, 3, 5]))
print(targetSum(300, [7, 14]))
