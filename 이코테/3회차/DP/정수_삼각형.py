import sys

input = sys.stdin.readline
n = int(input())
dp = [[0] * i for i in range(1, n + 1)]
graph = []
for i in range(n):
    array = list(map(int, input().split()))
    if i == 0:
        dp[0][0] = array[0]
    graph.append(array)

for x in range(1, n):
    for y in range(x + 1):
        if y == 0:
            dp[x][y] = graph[x][y] + dp[x - 1][y]
        elif y == x:
            dp[x][y] = graph[x][y] + dp[x - 1][y - 1]
        else:
            dp[x][y] = graph[x][y] + max(dp[x - 1][y], dp[x - 1][y - 1])

print(max(dp[n - 1]))