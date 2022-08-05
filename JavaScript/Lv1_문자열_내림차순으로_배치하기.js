function solution(s) {
  let answer = s.split("");
  answer.sort((a, b) => {
    if (a < b) return 1;
    if (a > b) return -1;
    if (a === b) return 0;
  });
  return answer.join("");
}
