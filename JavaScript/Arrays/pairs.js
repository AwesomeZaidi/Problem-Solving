const nums = [1,2,3]
const strs = ['one', 'two', 'three']

// this is good to map it but we  also want to flatten it.
// const mapped = nums.map( (val, index) => [ val, strs[index] ])

const flatMap = nums.flatMap( (val, index) => [ val, strs[index] ])

console.log(flatMap);
