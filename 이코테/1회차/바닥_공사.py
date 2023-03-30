n = int(input())
dp = [0] * 1001
dp[1] = 1
# 1 * 2 로 2개 2 * 2 로 1개 2 * 1 로 2개
dp[2] = 1 + 1 + 1

for i in range(3, n + 1):
    dp[i] = (dp[i - 1] + dp[i - 2] * 2) % 796796

print(dp[n])
