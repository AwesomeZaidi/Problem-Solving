// You are given a 2D array with integers. Write a function,
// count_negatives(input), which finds and returns the number
// of negative integers in the 2D array.

const arr =
[
    [0,1],
    [-1,2],
    [3,-4],
    [-9],
    [[[[[[-10]]]]]]
]

let totalNegatives = 0

arr.flat(Infinity).map((num) => num < 0 ? totalNegatives += 1 : null);

// Old/Broken Solution: this is unnessecary bc we don't need to allocate more mem for a new  arr
// const totalNegatives = arr.flat(Infinity).filter(num => num < 0);
