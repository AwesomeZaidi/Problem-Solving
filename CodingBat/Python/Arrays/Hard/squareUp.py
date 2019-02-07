# Given n>=0, create an array length n*n with the following pattern,
# shown here for n=3 : {0, 0, 1,    0, 2, 1,    3, 2, 1} (spaces added to show the 3 groups).
  
# squareUp(2) → [0, 1, 2, 1]
# squareUp(3) → [0, 0, 1, 0, 2, 1, 3, 2, 1]
# squareUp(4) → [0, 0, 0, 1, 0, 0, 2, 1, 0, 3, 2, 1, 4, 3, 2, 1]

def squareUp(n):
    currN = n-1
    counter = 1
    arr = []

    while currN > -1: #iterate through the num as many times as we need
        innerN = currN
        while innerN > 0: # add respective amount of zeros
            arr.append(0)
            innerN -= 1
        innerCounter = counter
        while innerCounter > 0: # add the numbers, incrementally
            arr.append(innerCounter)
            innerCounter -= 1
        
        currN -= 1
        counter += 1

    return arr


print(squareUp(4))