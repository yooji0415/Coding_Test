function solution(alp, cop, problems) {
  const answer = 0;
  let [maxAlp, maxCop] = [0, 0];
  problems.forEach((p) => {
    const [reqA, reqC, rwdA, rwdC, cost] = p;
    maxAlp = maxAlp < reqA ? reqA : maxAlp;
    maxCop = maxCop < reqC ? reqC : maxCop;
  });

  maxAlp = maxAlp < alp ? alp : maxAlp;
  maxCop = maxCop < cop ? cop : maxCop;

  // 행을 alp 값, 열을 cop 값으로 dp 어레이 생성
  const dp = Array.from(Array(maxAlp + 1), () =>
    Array(maxCop + 1).fill(Infinity)
  );
  dp[alp][cop] = 0;

  for (let nA = alp; nA <= maxAlp; nA++) {
    for (let nC = cop; nC <= maxCop; nC++) {
      if (nA !== 0)
        dp[nA][nC] =
          dp[nA - 1][nC] + 1 < dp[nA][nC] ? dp[nA - 1][nC] + 1 : dp[nA][nC];
      if (nC !== 0)
        dp[nA][nC] =
          dp[nA][nC - 1] + 1 < dp[nA][nC] ? dp[nA][nC - 1] + 1 : dp[nA][nC];

      problems.forEach((p) => {
        const [reqA, reqC, rwdA, rwdC, cost] = p;
        if (nA >= reqA && nC >= reqC) {
          const afterA = maxAlp < nA + rwdA ? maxAlp : nA + rwdA;
          const afterC = maxCop < nC + rwdC ? maxCop : nC + rwdC;
          dp[afterA][afterC] =
            dp[afterA][afterC] > dp[nA][nC] + cost
              ? dp[nA][nC] + cost
              : dp[afterA][afterC];
        }
      });
    }
  }

  return dp[maxAlp][maxCop];
}
