# Consider the leftmost and righmost appearances of some value in an array.
# We'll say that the "span" is the number of elements between the two inclusive.
# A single value has a span of 1. Returns the largest span found in the given array.
# (Efficiency is not a priority.)



# maxSpan([1, 2, 1, 1, 3]) → 4
# maxSpan([1, 4, 2, 1, 4, 1, 4]) → 6
# maxSpan([1, 4, 2, 1, 4, 4, 4]) → 6

# which one has the most occurances?

# find the index of the last last occurance in the arr and return that.

def maxSpan(arr):
    first = arr[0] # store 0th val
    last = arr[-1] # store last val

    firstCounter = 0
    firstIndex = 0
    lastCounter = 0
    lastIndex = 0
    # go through the array
    for i, e in enumerate(arr):
        if e == first:
            firstCounter += 1
            firstIndex = i+1
        if e == last:
            lastCounter += 1
            lastIndex = i+1

    if firstCounter > lastCounter:
        return firstIndex
    else:
        return lastIndex
        

print(maxSpan([1, 2, 1, 1, 3]))