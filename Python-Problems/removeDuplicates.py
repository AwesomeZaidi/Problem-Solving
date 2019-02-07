def removeDuplicates(nums):
    len = 0
    for index, num in enumerate(nums[:-1]):
        print("len:", len)
        print("index", index)

        print(nums)
        if nums[index] == nums[index+1]:
            # nums.pop(index+1) # shifts right
            index -= 1
            nums.append(nums.pop(index+1))
        else:
            len += 1
    
    return len


nums = [0,0,1,1,1,2,2,3,3,4]


print(removeDuplicates(nums))
print(nums)