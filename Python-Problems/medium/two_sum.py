def two_sum(nums, target):
    
    numsDict = dict( ((value, index) for index, value in enumerate(nums)) )
    print("numsDict:", numsDict) # keys: elements from list, value: index of elemennts from the list.

    for key, _ in enumerate(numsDict):
        complement = target - nums[key] # 4 - 2 = 2.
        print('key:', key, 'complement:', complement)
        if complement in numsDict: # Is 2 in our dictionary?
            print('complement is in dict.')
            printn('numsDict[complement]:', numsDict[complement])
            if numsDict[complement] != key:
                return nums[key], complement

# Calling Class
nums = [2,7,11,15]
target = 4
print(two_sum(nums, target))
