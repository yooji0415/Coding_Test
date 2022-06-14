import sys


N = int(sys.stdin.readline())
T = [0 for _ in range(N + 1)]
P = [0 for _ in range(N + 1)]
for i in range(N):
    ti, pi = map(int, sys.stdin.readline().split())
    T[i] = ti
    P[i] = pi

dp = [0 for _ in range(N + 1)]
for i in range(N - 1, -1, -1):
    if i + T[i] <= N:
        dp[i] = max(P[i] + dp[i + T[i]], dp[i + 1])
    else:
        dp[i] = dp[i + 1]

print(dp[0])
