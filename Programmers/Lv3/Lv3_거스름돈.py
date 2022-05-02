def solution(n, money):
    dp = [0] * (n + 1)
    dp[0] = 1
    for m in money:
        for p in range(m, n + 1):
            if p >= m:
                dp[p] += dp[p - m]
    return dp[n] % 1000000007