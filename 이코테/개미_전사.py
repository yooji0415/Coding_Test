n = int(input())
items = list(map(int, input().split()))

dp = [0] * (n + 1)
dp[0] = items[0]
dp[1] = max(items[0], items[1])

for i in range(2, n):
    dp[i] = max(dp[i - 1], dp[i - 2] + items[i])

print(dp[n - 1])
