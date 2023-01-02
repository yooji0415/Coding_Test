function solution(n, l, r) {
  let answer = 0;

  const checkFun = (start, end, n) => {
    if (end === start) {
      if (l <= start && start <= r) answer++;
      return;
    }
    const gap = 5 ** (n - 1);

    for (let i = 0; i < 5; i++) {
      if (i === 2) continue;

      const newStart = start + gap * i;
      const newEnd = start + gap * (i + 1) - 1;

      if (l <= newStart && newEnd <= r) {
        answer += 4 ** (n - 1);
        continue;
      }
      if (r < newStart || newEnd < l) continue;
      checkFun(newStart, newEnd, n - 1);
    }
  };

  checkFun(1, 5 ** n, n);

  return answer;
}
