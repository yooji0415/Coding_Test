function solution(maps) {
  const answer = [];
  const graph = [];
  const visited = [];
  const maxX = maps[0].length;
  const maxY = maps.length;
  const dx = [0, 0, 1, -1];
  const dy = [1, -1, 0, 0];

  maps.forEach((line) => {
    graph.push([...line]);
    visited.push(new Array(line.length).fill(false));
  });

  const bfs = (sX, sY) => {
    let total = parseInt(graph[sY][sX]);
    visited[sY][sX] = true;
    const queue = [[sY, sX]];
    while (queue.length !== 0) {
      const [Y, X] = queue.pop();
      for (let i = 0; i < 4; i++) {
        const [nY, nX] = [Y + dy[i], X + dx[i]];
        if (nY < 0 || nY >= maxY) continue;
        if (nX < 0 || nX >= maxX) continue;
        if (graph[nY][nX] === "X" || visited[nY][nX]) continue;
        visited[nY][nX] = true;
        total += parseInt(graph[nY][nX]);
        queue.push([nY, nX]);
      }
    }
    return total;
  };

  for (let y = 0; y < maxY; y++) {
    for (let x = 0; x < maxX; x++) {
      // 만약 해당 위치가 X면 넘어간다.
      if (graph[y][x] === "X") continue;
      // 만약 해당 위치가 이미 방문한 곳이면 넘어간다.
      if (visited[y][x]) continue;
      // 섬이면
      const result = bfs(x, y);
      answer.push(result);
    }
  }
  return answer.length === 0 ? [-1] : answer.sort((a, b) => a - b);
}
