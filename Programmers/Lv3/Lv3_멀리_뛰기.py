def solution(n):
    dp = {
        1: 1,
        2: 2,
        3: 3,
        4: 5
    }
    temp = 5
    while n not in dp:
        dp[temp] = dp[temp - 2] + dp[temp - 1]
        temp += 1

    return dp[n] % 1234567