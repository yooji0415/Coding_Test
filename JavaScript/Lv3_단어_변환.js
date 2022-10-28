const solution = (begin, target, words) => {
  if (!words.includes(target)) return 0;
  let answer = 0;
  const wordsList = [begin, ...words, target];
  // 우선 그래프 생성
  const graph = Array.from(Array(wordsList.length), () => new Array(0));
  for (let i = 0; i < wordsList.length - 1; i++) {
    const a = wordsList[i].split("");
    for (let j = i + 1; j < wordsList.length; j++) {
      const b = wordsList[j].split("");
      if (a.filter((_, idx) => a[idx] !== b[idx]).length === 1) {
        graph[i].push(j);
        graph[j].push(i);
      }
    }
  }
  // 이후 BFS
  const bfs = (graph) => {
    const visited = new Array(graph.length).fill(false);
    let needVistit = [];
    const lenList = new Array(graph.length).fill(50000);
    lenList[0] = 0;

    needVistit.push(0);
    while (needVistit.length !== 0) {
      const node = needVistit.shift();
      if (!visited[node]) {
        visited[node] = true;
        needVistit = [...needVistit, ...graph[node]];
        graph[node].forEach((n) => {
          if (lenList[n] > lenList[node] + 1) lenList[n] = lenList[node] + 1;
        });
      }
    }
    return lenList;
  };

  // 결과 확인
  const result = bfs(graph);
  console.log(result);
  return result[result.length - 1] >= 50000 ? 0 : result[result.length - 1];
};
