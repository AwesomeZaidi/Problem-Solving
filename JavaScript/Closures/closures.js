var a = 3;
var b = 10;
function outer() { // two a
    var  a = 1;
    function inner() {
        var b = 2;
        console.log(a + b); // two -> 3       
    }
    inner(); // two b
    console.log(a); // three -> 1
}
// first
console.log(a); // 1
outer(); // two
console.log(b); // four -> 10

// Expected output: 1,3,1,10