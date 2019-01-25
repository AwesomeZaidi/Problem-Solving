def twoSum(nums, target):
    # for i in nums:
    #     print ("i:", i)
    #     j = 1
    #     while j < len(nums):
    #         print ("j:", j)
    #         if j == target - i:
    #             return i, j
    #         j += 1

    for i in nums:
        for j in range(1, len(nums)):
            if nums[j] == target - i:
                return i, nums[j]
            j += 1
    
    raise ValueError("No two sum solution")

nums = [2,7,11,15]
target = 9
print(twoSum(nums, target))

        
# Given nums = [2, 7, 11, 15], target = 9,
