function solution(arr, divisor) {
  const answer = [];
  arr.sort((a, b) => {
    return a - b;
  });
  arr.forEach((value) => {
    if (value % divisor === 0) answer.push(value);
  });
  if (answer.length === 0) return [-1];
  return answer;
}
