import sys


N = int(sys.stdin.readline().strip())
stair = []
for _ in range(N):
    stair.append(int(sys.stdin.readline().strip()))

if N == 1:
    print(stair[0])
elif N == 2:
    print(stair[0] + stair[1])
else:
    dp = {
        0: stair[0],
        1: stair[0] + stair[1],
        2: max(stair[0] + stair[2], stair[1] + stair[2])
    }
    for i in range(3, N):
        dp[i] = max(dp[i - 2] + stair[i], dp[i - 3] + stair[i] + stair[i - 1])

    print(dp[N - 1])
