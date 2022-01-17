n = int(input())

dp = [0 for _ in range(n + 1)]

for i in range(2, n + 1):
    dp[i] = dp[i - 1] + 1

    if i % 2 == 0 and dp[i] > dp[i // 2] + 1:
        dp[i] = dp[i // 2] + 1

    if i % 3 == 0 and dp[i] > dp[i // 3] + 1:
        dp[i] = dp[i // 3] + 1

print(dp[n])

# 동일하게 아래에서 부터 올라가는 풀이지만
# 이것은 특정 대상의 숫자를 이전 자료를 통해서 풀었다.
# 좀 더 간결한 DP 풀이이다.
