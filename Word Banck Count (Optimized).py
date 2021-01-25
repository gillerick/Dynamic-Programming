"""
Count the number of times that a target string can be constructed from a bank of words
"""
def canCount(target, wordBank, memo={}):
    if target in memo:
        return memo[target]
    if target == "":
        return 1
    count = 0
    for word in wordBank:
        try:
            if target.index(word) == 0:
                suffix = target[len(word):]
                count += canCount(suffix, wordBank)
        except ValueError:
            pass
    memo[target] = count
    return count


print(canCount("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
print(canCount("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee", ["e", "eee", "eeee", "eeeeee", "eeeeeeeee"]))
