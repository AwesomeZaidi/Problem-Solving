# PROMPT
# "Johnny wen to the store" --> JWTTS
# "He _went_ _out"---> HWO
## Acornym should be all caps
## Only count for alphanumeric characters in the Acornym

# clarificationds: do you want the list to be from least to greatest or from greatest to least
# assumptions: multiply first then sort them, or first sort then multiply?
# Rules: first make it work then refactor; o notation and benchmarking
# NOTE: pseudocode first, then code, then refactor... talk to myself, or buy duck or hire prosititue to talk to


# check if the string doesn't contain any spaces
    # if so, grab the first character
        # check if it is alphanumeric
            # return that first char
        # otherwise
            # return "no alphanumeric acroynm char found, sorry!"
    

class Acronym():

    def __init__(self, word):
        self.word = word
        self.alphas = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ"
        self.acronym = ""

    def isAlphanumeric(self, character):
        # check if character exists in the string of characters with out a builtin method
        if character in self.alphas:
            return True
        else:
            return False

    def getAcronyms(self):
        
        if  self.isAlphanumeric(self.word[0]):
            self.acronym += self.word[0]

        for index, element in enumerate(self.word):
            if element == " " and self.isAlphanumeric(self.word[index+1]): # if we find a space & next char is alphanumeric
                acronym += self.word[index+1] # add it to the acronym string

        print("acronym:", acronym)
        return acronym
                

word = Acronym("Johnny wen to the store")
print(word.getAcronyms)
