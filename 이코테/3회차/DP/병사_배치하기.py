N = int(input())
soldiers = list(map(int, input().split()))
soldiers.reverse()

dp = [1] * N
for i in range(1, N):
    for j in range(i):
        if soldiers[i] > soldiers[j]:
            dp[i] = max(dp[i], dp[j] + 1)
print(N - dp[-1])
