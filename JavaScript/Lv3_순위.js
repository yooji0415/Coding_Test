function solution(n, results) {
  const graph = Array.from(Array(n + 1), () => Array(n + 1).fill(0));
  results.forEach((result) => {
    const [a, b] = result;
    // 이긴걸 2
    graph[a][b] = 2;
    graph[b][a] = 1;
  });

  for (let i = 1; i < n + 1; i++) {
    for (let j = 1; j < n + 1; j++) {
      for (let k = 1; k < n + 1; k++) {
        if (graph[j][k] === 0 && graph[j][i] === 1 && graph[i][k] === 1)
          graph[j][k] = 1;
        if (graph[j][k] === 0 && graph[j][i] === 2 && graph[i][k] === 2)
          graph[j][k] = 2;
      }
    }
  }

  let answer = 0;
  graph.shift();
  graph.forEach((line) => {
    const cnt = line.filter((e) => e === 0).length;
    if (cnt === 2) answer++;
  });

  return answer;
}
