
# Given a string of even length, return a string made of the middle two chars,
# so the string "string" yields "ri". The string length will be at least 2.


# middleTwo("string") → "ri"
# middleTwo("code") → "od"
# middleTwo("Practice") → "ct"

def middleTwo(word):
    l = len(word)
    hop = int((l/2) - 1)
    
    newWord = word[hop:l-hop]

    return newWord




useCase1 = "string"
useCase2 = "code"
useCase3 = "Practice"

print(middleTwo(useCase1))
print(middleTwo(useCase2))
print(middleTwo(useCase3))
