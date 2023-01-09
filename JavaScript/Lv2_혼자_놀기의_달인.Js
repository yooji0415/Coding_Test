function solution(cards) {
  const graph = {};
  cards.forEach((val, idx) => {
    graph[idx + 1] = val;
  });

  const visited = Array(cards.length + 1).fill(false);
  const group = [];

  const bfs = (start) => {
    const queue = [];
    let count = 0;

    if (visited[start]) return 0;

    visited[start] = true;
    queue.push(start);

    while (queue.length !== 0) {
      const now = queue.pop();
      count++;
      if (visited[graph[now]]) continue;
      visited[graph[now]] = true;
      queue.push(graph[now]);
    }

    return count;
  };

  for (let i = 1; i < cards.length + 1; i++) {
    const result = bfs(i);
    if (result !== 0) group.push(result);
  }

  group.sort((a, b) => b - a);
  return group.length < 2 ? 0 : group[0] * group[1];
}
