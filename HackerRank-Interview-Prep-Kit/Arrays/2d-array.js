//global variables
let n = 0;
let d = 0;
let data = [];

//read standard input
process.stdin.setEncoding("utf8");
process.stdin.resume();

let input = "";

// process.stdin returns a stream connected to net socket.
process.stdin.on("data", (data) => {
    input += data;
});

process.stdin.on("end", function() {
let linesOfInput = input.split("\n");
let temp = linesOfInput[0].split(" ");
temp.map(Number);
n = temp[0];
d = temp[1];
data = linesOfInput[1].split(" ");

main();
})