
def removeDuplicates(nums: 'List[int]') -> 'int':
    
    newSet = set()

    for i, e in reversed(list(enumerate(nums))):
        print("i:", i, "e:", e)
        print("newSet:", newSet)
        if e not in newSet:
            print(e, "is not in newSet")
            newSet.add(e)
            print("newSet", newSet)
        else:
            print(e, "is in newSet")
            print("nums:", nums)
            print("i:", i)
            nums.pop(i)
            print("new nums:", nums)

    return nums


print(removeDuplicates([1,1,2]))