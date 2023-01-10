const fs = require("fs");
// backjoon
// const readFileSyncAddress = "/dev/stdin";
// vscode
const readFileSyncAddress = "input.txt";

const inputs = fs
  .readFileSync(readFileSyncAddress)
  .toString()
  .trim()
  .split("\n");

const N = parseInt(inputs.shift());
const towers = inputs.map((tower) => Number(tower));

let answer = 0;
const stack = [];
towers.forEach((tower, idx) => {
  if (stack.length === 0) stack.push([tower, idx]);
  else {
    while (stack.length !== 0) {
      const topOfTower = stack.pop();
      if (topOfTower[0] <= tower) answer += idx - topOfTower[1] - 1;
      else {
        stack.push(topOfTower);
        break;
      }
    }
    stack.push([tower, idx]);
  }
});

if (stack.length !== 0) {
  while (stack.length !== 0) {
    const topOfTower = stack.pop();
    answer += N - topOfTower[1] - 1;
  }
}

console.log(answer);
