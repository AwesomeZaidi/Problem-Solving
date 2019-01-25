function getSecondLargest(nums) {
    // Complete the function
    var largestNumber = nums[0];
    sl = 0;
    for (let i = 1; i < nums.length; i++) {
        if (nums[i] > l) {
            sl = l;
            l = nums[i];
        }
        if (nums[i] > sl && nums[i] < l)
            sl = nums[i]; 
    }
    return sl; 
}

