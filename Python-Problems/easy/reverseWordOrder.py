def revWordOrder():
    word = input("What should we reverse for you today? ")
    wordReversed=""
    wordList = word.split()
    reversedWord = wordList[::-1]
    wordReversed=" ".join(reversedWord)
    return wordReversed

print(revWordOrder())
