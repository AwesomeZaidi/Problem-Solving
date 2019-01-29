
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
        if element in nums[index-1::-1]:
            continue
        else:
            totalUniqueCount += 1
            newArr.append(nums[index])
            continue

    return newArr


print(count_uniques([1,0,1,2,3,4,5,5]))

