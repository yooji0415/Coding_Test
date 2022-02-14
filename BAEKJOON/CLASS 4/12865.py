import sys

n, k = map(int, sys.stdin.readline().split())

item = [[0,0]]
for _ in range(n):
    w, v = map(int, sys.stdin.readline().split())
    item.append([w, v])

dp = [[0 for _ in range(k + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, k + 1):
        w = item[i][0]
        v = item[i][1]
        # 단일 무게가 배낭을 초과하는 경우
        if w > j:
            dp[i][j] = dp[i - 1][j]
        # 그렇지 않고 넣을 수 있는 경우
        else:
            dp[i][j] = max(dp[i - 1][j - w] + v, dp[i - 1][j])

print(dp[n][k])
