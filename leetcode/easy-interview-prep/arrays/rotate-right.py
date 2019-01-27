
def rotate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    # if we have k == 0, we don't need to do anything
    if k == 0:
        return
    
    # otherwise, slice out the items we want to rotate
    # and splice them back together
    length = len(nums)
    rotated_elems = nums[:-k % length]  # allows for rotation > length, using a mod
    beginning_elems = nums[length-k:]
    nums[:k], nums[k:] = beginning_elems, rotated_elems


# def rotate(self, nums, k):
#     steps = k % len(nums)
#     nums[:] = nums[-steps:] + nums[:-steps]

rotate([1,2,3,4,5,6,7,8,9], 10)