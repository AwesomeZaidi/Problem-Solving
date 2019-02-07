# Return true if the string "cat" and "dog" appear the same number of times in the given string.


# catDog("catdog") → true
# catDog("catcat") → false
# catDog("1cat1cadodog") → true

def catDog(word):
    catCounter = 0
    dogCounter = 0

    for i in range(len(word)-2):
        if word[i:i+3] == 'dog':
            dogCounter += 1
        
        if word[i:i+3] == 'cat':
            catCounter += 1

    if catCounter == dogCounter:
        return True
    else:
        return False

print(catDog("1cat1cadodog"))