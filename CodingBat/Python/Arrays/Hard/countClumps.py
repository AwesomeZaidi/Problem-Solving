# Say that a "clump" in an array is a series of 2 or more adjacent elements of the same value.
# Return the number of clumps in the given array.

# countClumps([1, 2, 2, 3, 4, 4]) → 2
# countClumps([1, 1, 2, 1, 1]) → 2
# countClumps([1, 1, 1, 1, 1]) → 1

def countClumps(arr):
    totalClumps = 0 # use this to tack the totalClumps
    clumpStart = 0 # use this var to compare with the iterator value in loop.
    clumpDuration = 0 # use this var to track the duration of the current clump

    for i in arr[1:]:

        if arr[clumpStart] != i:
            clumpDuration = 0
            clumpStart += 1
            continue

        if clumpDuration < 1:
            if arr[clumpStart] == i:
                clumpDuration += 1
                clumpStart += 1
                totalClumps += 1
                continue

    return totalClumps


print(countClumps([1, 2, 2, 3, 4, 4, 5, 5]))