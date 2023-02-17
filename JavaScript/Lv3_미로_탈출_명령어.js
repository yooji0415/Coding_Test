function solution(n, m, x, y, r, c, k) {
  let answer = "impossible";

  const dy = [0, -1, 1, 0];
  const dx = [1, 0, 0, -1];
  const alpha = ["d", "l", "r", "u"];

  const backTracking = (nowX, nowY, arr) => {
    // 만약 k개가 되었다면
    if (arr.length === k) {
      if (nowX !== r || nowY !== c) return false;
      answer = arr.join("");
      return true;
    }
    // 진행 중인 경우
    for (let i = 0; i < 4; i++) {
      const [nextX, nextY] = [nowX + dx[i], nowY + dy[i]];
      if (nextX < 1 || nextX > n) continue;
      if (nextY < 1 || nextY > m) continue;
      if (nextX === x && nextY === y) continue;

      arr.push(alpha[i]);
      if (backTracking(nextX, nextY, arr)) return true;
      arr.pop();
    }
    return false;
  };

  backTracking(x, y, []);
  return answer;
}
