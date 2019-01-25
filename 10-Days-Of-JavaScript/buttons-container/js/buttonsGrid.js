const body = document.getElementsByTagName("body")[0];
const totalButtons = 9;

for (i = 0; i < totalButtons; i++) {
    body.appendChild(eval("btn" + i + " = document.createElement('button')"));
    eval()
}