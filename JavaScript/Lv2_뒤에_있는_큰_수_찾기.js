function solution(numbers) {
  const answer = Array(numbers.length).fill(-1);
  const stack = [];
  // idx, val 순으로 stack에 쌓아준다.
  for (let i = 0; i < numbers.length; i++) {
    while (stack.length !== 0) {
      const [si, sv] = stack.pop();
      if (sv >= numbers[i]) {
        stack.push([si, sv]);
        break;
      }
      answer[si] = numbers[i];
    }

    stack.push([i, numbers[i]]);
  }
  return answer;
}
