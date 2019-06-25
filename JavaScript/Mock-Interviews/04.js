// PART 1



// Write a fucntion to get the sum of the perimeters of a matrix.
const matrix1 = [
    [1,1,1,1],
    [1,1,1,1],
    [1,1,1,1],
    [1,1,1,1],
];

// My pseudo code

// find length of matrix
// use that to understand the the perimeter indeces.

// 16

// 0-3, 4+3=7, 8+3=11,12-15

// matrixLen sq root it and grab the first square  root indece values, then the next val,
// then + the  sq root-1, then the next val, then the sq -1 until we reach the matrixLen-the sqroot, then add those last vals.

// My solution: GOT STUCK.

// const matrixLen = len(matrix1);
// const sqrt = Math.sqrt(matrixLen);
// for i
// for (let i = sqrt-1; i < matrixLen - sqrt; i++) {

// }



// PART 2




// console.log([1,2,3].reduce((c, v) => c + v));
// Build your own myReduce function!

Array.prototype.myReduce = function(fn, init) {
    // this array [1,2,3]
    // go over the  arr and every time, execute the fn
    // provide, this.current index and the init val.
    let current = init || this[0];
    for (let i=0; i < this.length; i++) {
        if (init == undefined) continue;
        current = fn(this[i], current)
    }
    return current
};

// console.log([1,2,3].myReduce((c, v) => c + v,0));



// PART 3



// Implement your own Promise, myPromise.


// My solution: UNFINISHED.

let MyPromise = function(fn ) {
    return (onSuccess, onError) => {

    }
}

let myPromise = new MyPromise((res, rej) => {
    // if () {
    //     resolve(val);
    // } else {
    //     reject(err)
    // }
})

// promise = new Promise(resolve, reject) => {

// });



// PART 4



console.log(f(1)(2)(3)); // 9
console.log(f(2)(2)(1)); // 4
console.log(f(2,2,1)); // 4
console.log(f()); // 0

function f(a,b,c) {
    if (a && b && c){
        return (a + b)  * c
    } else if (a  && b) {
        return function(val) {
            return (a + b) * val
        }
    } else if (a) {
        return function(val1) {
            return function(val2) {
                return (a + val1) * val2;
            }   
        }
    } else {
        return 0;
    }
}