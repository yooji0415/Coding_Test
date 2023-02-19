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

const T = parseInt(inputs.shift());

const dfs = (cycle, result, x, visited, nextArr) => {
  visited[start] = true;
  cycle.push(x);
  const number = nextArr[x];

  if (visited[number]) {
    const idx = cycle.indexOf(number);
    if (idx !== -1) result = [...result, ...cycle.slice(idx + 1)];
    return;
  }

  dfs(cycle, result, number, visited, nextArr);
};

const test = () => {
  let answer = 0;
  const N = parseInt(inputs.shift());
  const inputArr = inputs[0].map((value) => parseInt(value));
  const nextArr = [0, ...inputArr];
  const visited = Array.from(Array(N + 1), () => false);
  visited[0] = true;

  let result = [];
  for (let i = 1; i < N + 1; i++) {
    if (!visited[i]) {
      const cycle = [];
      dfs(cycle, result, i, visited, nextArr);
    }
  }
  console.log(N - result.length);
};

for (let i = 0; i < T; i++) {
  test();
}
