// PART 1

let ary = [1,2,,5,7]

// add em all to get the sum

console.log(ary.reduce( (acc, item) =>  acc + item))


// PART 1


// add(1,2)
// add(1)(2)
// Write one function that does this both ways.

function add(num1, num2) { 
    if (num1 && num2) {
        return num1 + num2
    } else {
        return function(num3) {
            return num1 + num3
        }
    }
}


// Part 3
// Unsorted array of 1-100, expect 1 number is missing

// let len = arr.len
// let total = n*(n+1) / 2

// let arrayTotal = ary3.reduce((t, i) => t + i)

// console.log(total-arrayTotal);


// PART 4


const til = {
    penny: 12,
    nickel: 10,
    dime: 2,
    quarter: 12,
    dollar: 30
}

// 20.47

function money(total) {
    // sub the whole dollars
    const dollar = til.dollar
    const quarter = til.quarter
    runningTotal = total
    for (let i = 0; i < til.len; i++) {
        if (runningTotal < dollar) {
            runningTotal = dollar - runningTotal
            continue
        }
    }

}

