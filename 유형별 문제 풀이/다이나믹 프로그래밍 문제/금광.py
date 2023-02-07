test_case = int(input())

for _ in range(test_case):
    n, m = map(int, input().split())
    graph = []

    temp = list(map(int, input().split()))
    if m == 1:
        print(max(temp))
        continue

    for i in range(0, n * m, m):
        graph.append(temp[i:i+m])

    dp = [[0] * m for _ in range(n)]
    col = 0
    while col < m:
        if col == 0:
            for i in range(n):
                dp[i][0] = graph[i][0]
            col += 1
            continue

        for i in range(n):
            candi = []
            for j in range(-1, 2):
                if 0 <= i + j < n:
                    candi.append(graph[i + j][col - 1] + graph[i][col])
            graph[i][col] = max(candi)

        col += 1

    score = 0
    for g in graph:
        print(g)

    for i in range(n):
        score = max(score, graph[i][m - 1])
    print(score)
