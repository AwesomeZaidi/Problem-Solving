
def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if (nums == None or len(nums) == 0):
        return 0
    totalUniqueCount = 0
    for index, element in enumerate(nums):
        if index == 0:
            totalUniqueCount += 1 
            continue
        if element in nums[index-1::-1]:
            continue
        else:
            totalUniqueCount += 1
            continue

    return totalUniqueCount


print(removeDuplicates([1,0,1,2,3,4,5,5]))

