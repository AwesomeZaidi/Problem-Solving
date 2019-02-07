
# Given two strings, append them together (known as "concatenation") and return the result.
# However, if the strings are different lengths,
# omit chars from the longer string so it is the same length as the shorter string.
# 
# So "Hello" and "Hi" yield "loHi". The strings may be any length.


# minCat("Hello", "Hi") → "loHi"
# minCat("Hello", "java") → "ellojava"
# minCat("java", "Hello") → "javaello"
#  given a list of numbers multiply them by 3 and put them in order
# input: [3, 7, 8, 2, 1, 10, 4, 5, 5, 6, 13, 34]

# clarificationds: do you want the list to be from least to greatest or from greatest to least
# assumptions: multiply first then sort them, or first sort then multiply?
# Rules: first make it work then refactor; o notation and benchmarking
# NOTE: pseudocode first, then code, then refactor... talk to myself, or buy duck or hire prosititue to talk to



def minCat(wordOne, wordTwo):
    # wordOneLen = len(wordOne)
    # wordTwoLen = len(wordTwo)
    # # switch case 
    # if (wordOneLen > wordTwoLen):
    #     wordCut = wordOne[len(wordOne)-wordTwoLen:]
    #     return wordCut + wordTwo
    # elif (wordTwoLen > wordOneLen):
    #     wordCut = wordTwo[len(wordTwo)-wordOneLen:]
    #     return wordOne  + wordCut
    # else:
    #     return wordOne + wordTwo

    


print(minCat("Hello", "Hi"))
print(minCat("Hello", "java"))
print(minCat("java", "Hello"))

# "Johnny wen to the store" --> JWTTS
# "He _went_ _out"---> HWO
## Acornym should be all caps
## Only count for alphanumeric characters in the Acornym