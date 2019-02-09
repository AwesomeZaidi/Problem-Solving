#!python3


def three_sum(arr):
    """Simple test cases in docstring
    >>> three_sum([2, -2, 0])
    [2,-2, 0]
    >>> three_sum(3)
    [0, 0, 1, 0, 2, 1, 3, 2, 1]
    >>> three_sum(4)
    [0, 0, 0, 1, 0, 0, 2, 1, 0, 3, 2, 1, 4, 3, 2, 1]
    >>> three_sum(5)
    [0, 0, 0, 0, 1, 0, 0, 0, 2, 1, 0, 0, 3, 2, 1, 0, 4, 3, 2, 1, 5, 4, 3, 2, 1]
    """
    triplets = []

    # outer loop will go from first element to next to last element
    for i in range(len(arr)-1):

        # we need a set to hold elements previously visited
        s = set()

        # inner loop will go from second element to last element
        for j in range(i+1, len(arr)):

            # to get 0 we need two numbers that add up to be the positive
            # inverse of a negative number
            if -(arr[i] + arr[j]) in s:
                # we are appending a list of [the previously visited number, current, next]
                triplets.append([-(arr[i] + arr[j]), arr[i], arr[j]])
            else:
                s.add(arr[j])
                print("Set:", s)    
    # return triplets
    return triplets


arr = [0, -1, 2, -3, 1, 4, 9, 12, 11, -11, 1]
result = three_sum(arr)
print(arr)
for i in result:
    print(i, "= 0")