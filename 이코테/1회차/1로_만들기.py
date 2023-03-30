x = int(input())
dp = [30000 for _ in range(x + 1)]

dp[1] = 0
for i in range(1, x):
    next_target = [i + 1, i * 2, i * 3, i * 5]
    for n in next_target:
        if n > x:
            continue
        if dp[n] > dp[i] + 1:
            dp[n] = dp[i] + 1

print(dp[x])
