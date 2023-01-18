function solution(ability) {
  let answer = 0;
  const N = ability.length;
  const M = ability[0].length;

  const dfs = (selected, total, col) => {
    if (selected.length === M) {
      if (answer < total) answer = total;
      return;
    }

    // 초기 시작시
    if (selected.length === 0) {
      for (let i = 0; i < N; i++) {
        dfs([i], ability[i][0], 1);
      }
      return;
    }
    // 아닌 경우
    for (let i = 0; i < N; i++) {
      if (selected.includes(i)) continue;
      dfs([...selected, i], total + ability[i][col], col + 1);
    }
  };

  dfs([], 0, 0);

  return answer;
}
