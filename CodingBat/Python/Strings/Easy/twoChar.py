
# Given a string and an index, return a string length 2 starting at the given index.
# If the index is too big or too small to define a string length 2, use the first 2 chars.
# The string length will be at least 2.


# twoChar("java", 0) → "ja"
# twoChar("javaza", 2) → "va"
# twoChar("java", 3) → "ja"

def twoChar(word, index):
    # l = int(len(word))
    if index >= len(word)-1:
        return word[:2]
    return word[index:index+2]


print(twoChar("java", 0))
print(twoChar("java", 2))
print(twoChar("java", 3))