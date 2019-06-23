let str = 'asim'

// console.log([...str]);
const fromString = Array.from(str)

console.log(fromString);

// const fromStratch = Array.from({length: 5}, (v, i) => v)
const fromStratch = (new Array(5).fill(0))

console.log(fromStratch);

const ary = [1,1,2]

const unique = Array.from(new Set(ary))
const unique_2 = [...new Set(ary)]

console.log(unique);

console.log(unique_2);
