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

// 입력 정리
const n = parseInt(inputs[0]);
const towers = inputs[1].split(" ").map((value) => parseInt(value));
// 스택, 답 어레이 생성
const stack = [];
const answer = new Array(n).fill(0);

// 뒤부터 담는다
// 만약 현 위치의 타워가 전보다 높다? -> 스택에서 빼준다.
// 아닌 경우에는 stack 에 담는다.
while (towers.length) {
  const nowIdx = towers.length - 1;
  const nowHeight = towers.pop();
  //스택이 비었을 경우
  if (!stack.length) {
    stack.push([nowHeight, nowIdx]);
    continue;
  }
  // 스택이 있는 경우 뺄거는 뺀다.
  while (stack.length) {
    const [topOfStackHeight, topOfStackIdx] = stack.pop();
    if (topOfStackHeight < nowHeight) answer[topOfStackIdx] = nowIdx + 1;
    else {
      stack.push([topOfStackHeight, topOfStackIdx]);
      break;
    }
  }
  // 마지막으로 현 타워 정보를 넣어준다.
  stack.push([nowHeight, nowIdx]);
}

console.log(answer.join(" "));
