N = int(input())
graph = []
for i in range(N):
    time, cost = map(int, input().split())
    graph.append((time, cost))

dp = [0] * (N + 5)

for i in range(N - 1, -1, -1):
    time, cost = graph[i]
    if i + time > N:
        cost = 0
    dp[i] = max(dp[i + time] + cost, dp[i + 1])

print(dp[0])
