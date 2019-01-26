# Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

# Given nums = [1,1,2],

# Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.

# It doesn't matter what you leave beyond the returned length.

def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # Checking edge case
    if (nums == None or len(nums) == 0):
        return 0
    
    firstNum = nums[0]
    totalCount = 1
    for iter in range(1, len(nums)):
        print("iteration:", iter)
        print("firstNum:", firstNum)
        print("nums[iter]:", nums[iter])
        # If, our first num in arr is the same as the next element, do nothing
        if firstNum == nums[iter]:
            print("above nums [iter] and occur are the same")
            continue
        else:
            print("we found a new unique number!")
            # nums[iter] = nums[index]
            # print("new nums[iter]:", nums[iter])
            totalCount+=1
            firstNum = nums[iter]
            print("firstNum:", firstNum)
    
    return totalCount

    # Psuedocode

    # setting var firstNum: as the first element
    # create an totalCount starting at 1

    # loopthrough the array starting from the firstith element till the end
        # check if the element firstNum is the same as the next element, nums[iter]
            # if so , do nothing.
        # else
            # we have a new unique number.
            # add 1 to our totalCount counter
            # move occur up by one by setting it equal to nums[iter]

    
    # return that totalCount counter


print(removeDuplicates([2,3,4,4,5]))

        