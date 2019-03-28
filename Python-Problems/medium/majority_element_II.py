# Majority Element II
# Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

# Note: The algorithm should run in linear time and in O(1) space.

# Example 1:

# Input: [3,2,3]
# Output: [3]
# Example 2:

# Input: [1,1,1,3,3,2,2,2]
# Output: [1,2]

def maj_elem(numsArr):
    """
        Args: list of integers
        Returns: `values`: list of ints that appear more than n/3 times
    """

    numsArr.sort()
    min = len(numsArr) / 3
    print('min is:', min)
    i = 0
    count = 1
    print('numsArr:', numsArr)
    while i < len(numsArr)-1:
        print('i:', i, 'count:', count)
        if count > min:
            print('count less than min:', min)
            count = 1
            i += 1
            pass
        if numsArr[i] == numsArr[i+1]:
            print('match found')
            count += 1
            numsArr.pop(i)
            print('new numsArr:', numsArr)
        else:
            print('no match, pop element.')
            numsArr.pop(i)
            print('new numsArr:', numsArr)
            count = 1
    
    if count == 2 and i == len(numsArr):
        numsArr.pop(i)
            
    
    return numsArr

print(maj_elem([1,1,1,3,3,3,2,2]))
