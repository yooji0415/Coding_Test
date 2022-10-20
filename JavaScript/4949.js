const fs = require("fs");
// backjoon
// const readFileSyncAddress = "/dev/stdin";
// vscode
const readFileSyncAddress = "input.txt";

const input = fs
  .readFileSync(readFileSyncAddress)
  .toString()
  .trim()
  .split("\n");

const open = ["(", "["];
const close = [")", "]"];
let stack;
const results = [];
input.slice(0, input.length - 1).forEach((v) => {
  let isNo = false;
  stack = [];
  for (let i = 0; i < v.length; i++) {
    if (open.includes(v[i])) stack.push(v[i]);
    else if (close.includes(v[i])) {
      if (stack.pop() !== open[close.indexOf(v[i])]) {
        results.push("no");
        isNo = true;
        break;
      }
    }
  }
  if (!isNo) {
    if (stack.length === 0) results.push("yes");
    else results.push("no");
  }
});
console.log(results.join("\n"));
