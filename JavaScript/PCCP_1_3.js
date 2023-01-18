function getGene(pose) {
  let [n, p] = pose;
  let stack = [];

  p--; // 인덱스는 0부터 시작
  while (n > 1) {
    stack.push(p % 4); // 몇 번째 형제인지 저장
    n--;
    p = parseInt(p / 4); // 부모로 이동
  }

  while (stack.length > 0) {
    // 최상위 부모부터 pop
    num = stack.pop();
    if (num == 0) return "RR";
    if (num == 3) return "rr";
  }
  return "Rr";
}

function solution(queries) {
  return queries.map(getGene);
}
