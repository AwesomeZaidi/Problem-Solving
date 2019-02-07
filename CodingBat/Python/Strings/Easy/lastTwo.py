# Given a string of any length, return a new string where the last 2 chars,
# if present, are swapped, so "coding" yields "codign".


# lastTwo("coding") → "codign"
# lastTwo("cat") → "cta"
# lastTwo("ab") → "ba"

def lastTwo(word):
    return word[:-2] + word[-1] + word[-2]
    # word = list(word)
    # # this only works for lists
    # word[-2], word[-1] = word[-1], word[-2]

    # return ''.join(word)

print(lastTwo("coding"))
lastTwo("cat")
lastTwo("ab")
