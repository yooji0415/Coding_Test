const fs = require("fs");
const { exit } = require("process");
// backjoon
// const readFileSyncAddress = "/dev/stdin";
// vscode
const readFileSyncAddress = "input.txt";

const inputs = fs
  .readFileSync(readFileSyncAddress)
  .toString()
  .trim()
  .split("\n");

const dotCnt = parseInt(inputs[0]);

const dots = [];

inputs.slice(1, inputs.length).forEach((cordinates) => {
  dots.push(cordinates.split(" ").map((item) => Number(item)));
});

let answer = "";

dots
  .sort((a, b) => {
    if (a[1] === b[1]) return a[0] - b[0];
    return a[1] - b[1];
  })
  .forEach((cordinate) => {
    answer += cordinate.join(" ") + "\n";
  });

console.log(answer);
