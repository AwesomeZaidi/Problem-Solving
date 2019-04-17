
def count_uniques(nums):
    """
    :type nums: List[int]
    :rtype: int
    
    Now we need to change this to not count total unique values
    But rather return a new array of unique elements.
    """
    if (nums == None or len(nums) == 0):
        return []
    totalUniqueCount = 0
    newArr = []
    for index, element in enumerate(nums):
        if index == 0:
            totalUniqueCount += 1
            newArr.append(nums[index])
            continue
        if element in newArr:
            continue
        else:
            totalUniqueCount += 1
            newArr.append(nums[index])
            continue

    return newArr, totalUniqueCount

print(count_uniques([0,0,1,1,1,2,2,3,3,4]))

# ----------- PSEUDO CODE -------------  #

# if the arr is empty
    # return 0
# for every element in the given arr of numbers
    # if its the first element
        # append it to the new arr
        # increment unique count
        # continue
    # if element is in our new arr
        # continue
    # else
        # increment unique count
        # append it to the new arr
        # continue