// PART 1


let x = {
    a:1,
    b:2
};

// Convert the above object to an array of the values only.

// returns 2 dimensional arr
// const xArr = Object.entries(x)
// console.log('xArr:', xArr)

let xArr = []

for  (let i in x) {
    xArr.push(i)
}

let a = [1,3,4]

let g = {}

for (let item in a) {
    g[item] = false
}

console.log('g:', g)


// PART 2
// Reverse a string


let y = "hi";
let w = "iH"
// return "ih"

// Ideas:
    // build in reverse
    // splice through reverse and create a new var

// Solution

const reverseString = (str) => str.split('').reverse().join('')

console.log(reverseString(y).toLowerCase() === w.toLowerCase());
// Secondly, deal with lowercase elements.


// PART 3
// How would u fix this below code so it would print both a and b's values.
// const u = {
//     a:1,
//     b:2,
//     getA() {
//         console.log(this.a);
//     },
//     getB() {
//         console.log(this.b);
//     }
// }

const u = {
    a:1,
    b:2,
    getA() {
        console.log(this.a);
        return this;
    },
    getB() {
        console.log(this.b);
    }
}

const p = u.getA().getB();


// PART 4 - Level 7 shit.


// Array.prototype.print = () => {
//     let result = ''
//     for (let [i, elem] of this) {
//         if (i === this.length) {
//             result += elem
//         } else {
//             result += `${elem}`
//         }
//     }
//     // this next line, leaves a trailing comma at the end.
//     // So instead we go thru and just check if the index is at the end, do it without the comma.
//     // Or simpler answer, you could convert the list to a string with join by comma sperated values.
//     // this.forEach(elem => result += `${elem},`);
//     console.log(result);
// }


// [1,2].print(); // 1,2



// PART 5
// These methods below should have getters.
// How would you use inheritance?


// this shit is fucky still.
// const a = function(x) {
//     this.x = x;
//     this.x = new a(x).x
//     // or, even more es6 gang related
//     a.call(this, x)
// };

// a.prototype = {
//     getX() {
//         return this.s
//     }
// }

// const b = function(x, y) {
//     this.y = y;
// }

// const newB = new b('x', 'y');

// newB.getX();
// newB.getY();



// Level 8


const obj = {
    a: {
        b: {
            c:1
        }
    }
}

const clone = JSON.parse(JSON.stringify(obj))

clone.a.b.c = 2

console.log('obja.b.c:', obj.a.b.c); // should not give 2

// Level 8

// const a = [1,2,4,7,9]
// const a = [2,5,6,7,7,100]

// const b = [1,2,2,4,5,6,7,7,7,9,100]

// // use some built ins to do so but without the buit ins...
// // First Approach
// // spread operator (or optionally concat()) to join the two lists and then sort the result.

// // O(n log n) time & O(n) space
// function mergeTwo(arr1, arr2) {
//   let result = [...arr1, ...arr2];
//   return result.sort((a,b) => a-b);
// }

// // Greedy Approach
// // But given that the two arrays are already sorted we can use a greedy approach to go
// // through each array and track the smallest element, each time adding it to a new merged array.

// // O(n) time & O(n) space
// function mergeTwo(arr1, arr2) {
//     let merged = [];
//     let index1 = 0;
//     let index2 = 0;
//     let current = 0;
// } 


// Level 9:


const obj1 = {
    x:1,
    getX() {
        const that = this;
        const inner = function() {
            console.log(that.x);
        }
        // inner(); or
        inner.bind(this)();
    }
}

obj1.getX() // should give you undefined.

// SOlutioins?
// Changing the function to an arrow function
// But in babel it gets compiled down to function so then we