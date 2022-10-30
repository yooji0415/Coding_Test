function solution(A, B) {
  let answer = 0;
  const sortedA = A.sort((a, b) => a - b);
  const sortedB = B.sort((a, b) => a - b);
  let [startA, endA] = [0, sortedA.length - 1];
  let idxB = 0;
  while (idxB < sortedB.length) {
    if (sortedA[startA] < sortedB[idxB]) {
      answer += 1;
      idxB += 1;
      startA += 1;
      continue;
    }
    idxB += 1;
    endA -= 1;
  }
  return answer;
}
