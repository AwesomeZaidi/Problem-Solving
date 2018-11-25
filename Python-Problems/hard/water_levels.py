import math

# this solution is the most efficient and doesn't create any additional memory.
# this function runs in linear time as we have to go through every element.
def water_levels(arr):
    '''
        This function will take in an array representing land and return a sum of how water
        would be filled up if it were to rain in all of the land.
        
        Args: array (represents the land heights)

        Returns: sum (represents amount of water filled up)

        Need help visualizing this? Draw a bar graph and program trace every iteration.
    '''
    # this var will keep track of the largest spot in the array globally
    largest_index = 0;

    # we'll use index as the starting variable to loop through the array
    # it's value will be reset and changed later before later
    index = 1
    sum = 0

    # this loop will go through every element index in array and by the end, set the largest index in array.
    while index < len(arr):
        # if the value at that index is greater than the value at our largest index
        if arr[index] > arr[largest_index]:
            # set the largest index to that index
            largest_index = index
        # iterate index
        index+=1

    # reset i as we prepare to loop through the array from the left side.
    # i is 1, not 0 because we will never fill up water on the 0th index so we can skip that, save time.
    index = 1
    # this var is going be the largest value from the left side of the array.
    largestFromLeft = arr[0]
    # this loop will go through every element index from the leftside up until our largest index only!
    while index < largest_index:
        # sum will use max to add to itself the highest value of the largestFromLeft - the current arr[index] (max is a builtin math function)
        sum += max(largestFromLeft - arr[index], 0)
        # if a value is greater than our current largest value to the left
        if arr[index] > largestFromLeft:
            # reset that largest value
            largestFromLeft = arr[index]
        index+=1

    # now we set index = to the 2nd to last element of array,
    # since again our index doesn't care about the 1st and last element as we won't be adding water to them.
    index = len(arr) - 2
    # set the largest value from the right of the array
    largestFromRight = arr[len(arr)-1]
    # loop through array from the right side this time, going backwards until we reach our global max
    while index > largest_index:
        # using max again to add the largest of these 2 value to sum
        sum += max(largestFromRight - arr[index], 0)
        # if we find a value greater, let's reset largest from right/
        if arr[index] > largestFromRight:
            largestFromRight = arr[index]
        index-=1

    # THAT'S OUR SUM, SON!
    return sum


# this is the broken solution that Yves and myself white boarded
# it's only accounting for the largest value from the left
def broken_water_levels(arr):
    ed_a = arr[0]
    ed_b = arr[-1]

    i = ed_a
    sum = 0
    # for every index and item in an arr
    for index,item in enumerate(arr):
        if index == len(arr)-1:
            return sum
        # print("index:",index)
        # print("i:",i)
        # print ("sum:",sum)
        # if we reached the end of the loop, exit.
        # if index == len(arr)-1
        if i == 0:
            print("i == 0")
            print("changing i")
            i = arr[index+1]
            print("i =",i)
            continue
        elif i > arr[index+1]:
            sum += i - arr[index+1]
            continue
        elif i < arr[index+1]:
            i = arr[index+1]
            continue
    return sum

use_case_1 = [2,0,1,6,2,4,8,9]
use_case_2 = [2,1,3,1,5,1,1,2]
# print(broken_water_levels(use_case_1))
# print(broken_water_levels(use_case_2))

print(waterLevels(use_case_1))
print(waterLevels(use_case_2))
