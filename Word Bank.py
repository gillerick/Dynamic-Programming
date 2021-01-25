def canConstruct(target, wordBank):
    if target == "":
        return True
    for word in wordBank:
        # Check if substring is index of word
        try:
            if target.index(word) == 0:
                suffix = target[len(word):]
                if canConstruct(suffix, wordBank) == True:
                    return True
        except ValueError:
            pass
    return False

print(canConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
