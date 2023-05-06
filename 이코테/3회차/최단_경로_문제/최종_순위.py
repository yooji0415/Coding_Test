import sys
from collections import deque

input = sys.stdin.readline
tc = int(input())
for _ in range(tc):
    n = int(input())
    before = list(map(int, input().split()))

    indegrees = [0] * (n + 1)
    graph = [[False] * (n + 1) for _ in range(n + 1)]
    for a in range(n - 1):
        for b in range(a + 1, n):
            win, lose = before[a], before[b]
            graph[win][lose] = True
            indegrees[lose] += 1

    m = int(input())
    for _ in range(m):
        a, b = map(int, input().split())
        if graph[a][b]:
            graph[a][b] = False
            graph[b][a] = True
            indegrees[b] -= 1
            indegrees[a] += 1
        else:
            graph[a][b] = True
            graph[b][a] = False
            indegrees[b] += 1
            indegrees[a] -= 1

    q = deque()
    for num in range(1, n + 1):
        if indegrees[num] == 0:
            q.append(num)

    certain = True
    cycle = False
    result = []
    for _ in range(n):
        if len(q) > 1:
            certain = False
            break
        if not q:
            cycle = True
            break

        now = q.popleft()
        result.append(str(now))
        for i in range(1, n + 1):
            if graph[now][i]:
                graph[now][i] = False
                indegrees[i] -= 1
                if indegrees[i] == 0:
                    q.append(i)

    if cycle:
        print("IMPOSSIBLE")
    elif not certain:
        print("?")
    else:
        print(" ".join(result))
