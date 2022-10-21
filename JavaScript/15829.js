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

const [n, str] = inputs;
let hash = 0;
let r = 1;
for (let i = 0; i < str.length; i++) {
  hash += (str.charCodeAt(i) - 96) * r;
  hash %= 1234567891;
  r *= 31;
  r %= 1234567891;
}

console.log(hash);
