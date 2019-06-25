// PART 2


let x = 1234 // find the len = 4. Don't convert it to  a string.

function findNumLen(num) {
    let numLength = 0;
    while (num <9) {
        num = num / 10
        numLength++;
    }

    return numLength
}

console.log(findNumLen(x))