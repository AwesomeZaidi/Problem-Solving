import math

def waterLevels(arr):

    largest_index = 0;

    index = 1
    sum = 0
    

    while index < len(arr):
        if arr[index] > arr[largest_index]:
            largest_index = index
        index+=1

    index = 1
    largestFromLeft = arr[0]
    while index < largest_index:
        sum += max(largestFromLeft - arr[index], 0)
        if arr[index] > largestFromLeft:
            largestFromLeft = arr[index]
        index+=1

    index = len(arr) - 2
    largestFromRight = arr[len(arr)-1]
    while index > largest_index:
        sum += max(largestFromRight - arr[index], 0)
        if arr[index] > largestFromRight:
            largestFromRight = arr[index]
        index-=1

    return sum


def water_levels(arr):
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
# print(water_levels(use_case_1))
# print(water_levels(use_case_2))

print(waterLevels(use_case_1))
print(waterLevels(use_case_2))
