def canConstruct(target, wordBank, memo={}):
    if target in memo:
        return memo[target]
    if target == "":
        return True
    for word in wordBank:
        # Check if substring is index of word
        try:
            if target.index(word) == 0:
                suffix = target[len(word):]
                if canConstruct(suffix, wordBank, memo) == True:
                    memo[target] = True
                    return True
        except ValueError:
            pass
    memo[target] = False
    return False

print(canConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
print(canConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee", ["e", "ee", "eee", "eeee", "eeeeeee"]))
