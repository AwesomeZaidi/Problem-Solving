
def rotateString(A, B):
#         if both aren't the same len return False
    if len(A) != len(B):
        return False
#         Convert both strings into a list        
    # A = list(A)
    # B = list(B)
#         Run a function to move the the first char to the last of the list
#         Run this len(arr) amount of times
    for _ in range(len(A)):
        # A.append(A[0])
        A = A + A.index(0)
        # A.pop(0)
        A = A + A.index(0)

        if A == B:
            return True
    
    return False

print(rotateString('abcde', 'cdeab'))