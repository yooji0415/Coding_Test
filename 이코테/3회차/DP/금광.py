import sys

input = sys.stdin.readline
tc = int(input())
for _ in range(tc):
    n, m = map(int, input().split())
    graph = []
    dp = [[0] * m for _ in range(n)]
    array = list(map(int, input().split()))
    for i in range(n):
        graph.append(array[i * m : (i + 1) * m])
        dp[i][0] = array[i * m]
    for y in range(1, m):
        for x in range(n):
            if x == 0:
                dp[x][y] = max(dp[x][y - 1], dp[x + 1][y - 1]) + graph[x][y]
            elif x == n - 1:
                dp[x][y] = max(dp[x][y - 1], dp[x - 1][y - 1]) + graph[x][y]
            else:
                dp[x][y] = max(dp[x][y - 1], dp[x + 1][y - 1], dp[x - 1][y - 1]) + graph[x][y]

    answer = 0
    for x in range(n):
        answer = max(dp[x][m - 1], answer)
    print(answer)