def removeDuplicates(nums):
    len = 1
    newArr = []

    for index, num in enumerate(nums[:-1]):
        # print("len:", len)
        # print("index", index)

        # print(nums)
        if nums[index] == nums[index+1]:
            # nums.pop(index+1) # shifts right
            newArr.append(nums[index+1])
            nums.append(nums[index+1])
        else:
            len += 1
    
    for index in newArr:
        nums.pop(index)
    
    return len



nums = [0,0,1,1,1,1,2,2,3,3,4]


print(removeDuplicates(nums))
print(nums)

# def test(nums):

#     len = 0
#     newArr = []

#     for i,e in enumerate(nums[:-1]):

#         if nums[i] in newArr:
#             continue
#         else:
#             if nums[i] == nums[i+1]:
#                 newArr.append(nums[i+1])
#             else:
#                 len+=1