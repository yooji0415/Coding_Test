function solution(x, y, n) {
  if (x === y) return 0;
  const dp = Array(y + 1).fill(Infinity);
  dp[x] = 0;
  for (let i = x; i < y; i++) {
    const candidate = [i + n, i * 2, i * 3];
    candidate.forEach((val) => {
      if (val <= y) {
        dp[val] = dp[val] > dp[i] + 1 ? dp[i] + 1 : dp[val];
      }
    });
  }
  return dp[y] === Infinity ? -1 : dp[y];
}
