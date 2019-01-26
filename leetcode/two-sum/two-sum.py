class TwoSum():
    def __init__(self):
        pass

    def bruteForceWithRange(self, nums, target):
        '''
            Complexity Analysis
            Time complexity : O(n^2) For each element, we try to find its complement by looping through the rest of array which takes O(n)O(n) time. Therefore, the time complexity is O(n^2).
            Space complexity : O(1)O(1).
        '''
        for i in nums:
            for j in range(1, len(nums)):
                if nums[j] == target - i:
                    return i, nums[j]
                j += 1
        raise ValueError("No two sum solution") 
    
    def bruteForceWithWhile(self, nums, target):
        '''
            Complexity Analysis
            Time complexity : O(n^2) For each element, we try to find its complement by looping through the rest of array which takes O(n)O(n) time. Therefore, the time complexity is O(n^2).
            Space complexity : O(1)O(1).
        '''
        for i in nums:
            j = 1
            while j < len(nums):
                if j == target - i:
                    return i, j
                j += 1
        raise ValueError("No two sum solution")

    def hashMapTwoPass(self, nums, target):
        # create a dictionary with nums values and index
        numsDict = dict(  ( (v, i) for i, v in enumerate(nums) )  )

        print("numsDict:", numsDict)

        for index, value in enumerate(numsDict):
            print("index:", index, "value:", value)

            complement = target - nums[index]
            if complement in numsDict:
                if numsDict[complement] != index:
                    return nums[index], complement
        
        raise ValueError("No two sum solution")
            

# Calling Class
nums = [2,7,11,15]
target = 4
twoSum = TwoSum()

# print(twoSum.bruteForceWithRange(nums, target))

print(twoSum.hashMapTwoPass(nums, target))
