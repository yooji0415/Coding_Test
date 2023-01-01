function solution(queue1, queue2) {
  let answer = 0;
  // 일단 합을 구한다.
  let sumQ1 = queue1.reduce((acc, cur) => acc + cur, 0);
  let sumQ2 = queue2.reduce((acc, cur) => acc + cur, 0);
  // 두 합이 홀수인 경우 -1 처리
  if ((sumQ1 + sumQ2) % 2) return -1;
  // 아닌경우는 만들어야 하는 합을 구한다.
  const targetSum = (sumQ1 + sumQ2) / 2;
  // 어레이 붙이기
  const totalQ = [...queue1, ...queue2];

  let start = 0;
  let end = queue1.length - 1;
  let sum = sumQ1;
  while (sum !== targetSum && end >= start) {
    // console.log(`start: ${start} end: ${end} sum: ${sum} ${targetSum}`);
    if (sum > targetSum) {
      sum -= totalQ[start];
      start++;
      answer++;
      continue;
    }
    if (sum < targetSum) {
      if (end === totalQ.length - 1) break;
      end++;
      sum += totalQ[end];
      answer++;
      continue;
    }
  }

  return sum === targetSum ? answer : -1;
}
