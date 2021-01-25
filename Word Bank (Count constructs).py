def countConstructs(target, wordBank):
    if target == "":
        return [[]]
    constructs = [[]]
    for word in wordBank:
        try:
            if target.index(word) == 0:
                suffix = target[len(word):]
                suffixWays = countConstructs(suffix, wordBank)
                targetWays = map(int, suffixWays)
                constructs.append(targetWays)
        except ValueError:
            pass

print(countConstructs("abcdef", ["ab", "abc", "cd", "def", "abcd"]))


