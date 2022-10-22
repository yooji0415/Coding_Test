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

const [n, m] = inputs[0].split(" ").map((value) => Number(value));

const passwordBook = {};

inputs.slice(1, n + 1).forEach((value) => {
  const [site, password] = value.split(" ");
  passwordBook[site] = password;
});

const answer = [];
inputs.slice(n + 1, inputs.length).forEach((value) => {
  answer.push(passwordBook[value]);
});

console.log(answer.join("\n"));
