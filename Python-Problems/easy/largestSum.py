# Give an array, find the largest sum of a contiguous sobsequence

def largestSum(arr):
    # Questions?
        # What is cont subsequence? What sub array within the array if you added them would be the largest
    # Yuo need to identify it it'll be minus or plus, so keep track of the sum iterator.
    # sum the entire array, take a number off, sum that array, bounce around this array and check the sum val.
    # you might be able to like merge slice this array until you get to one or one
    # all the solutions involve looking at each element more than one time.
    # less than n square solution?
    # start with the left most and right most integers.
    # Sams solutions was OP.

    # Good clarfying questions would've been? Are they in any particular order,
    # positive or negative integer or zero? 

    # Determin brute forec

usecase1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]