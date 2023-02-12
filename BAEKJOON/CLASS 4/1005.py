from collections import deque
import sys

input = sys.stdin.readline

tc = int(input())
for _ in range(tc):
    n, k = map(int, input().split())
    time = list(map(int, input().split()))
    time = [0] + time

    in_degree = [0] * (n + 1)
    graph = [[] for _ in range(n + 1)]
    result = time[:]

    for _ in range(k):
        a, b = map(int, input().split())
        in_degree[b] += 1
        graph[a].append(b)

    w = int(input())


    def topology_sort():
        q = deque()

        for i in range(1, n + 1):
            if in_degree[i] == 0:
                q.append(i)

        while q:
            now = q.popleft()
            for node in graph[now]:
                result[node] = max(result[node], result[now] + time[node])
                in_degree[node] -= 1
                if in_degree[node] == 0:
                    q.append(node)

        print(result[w])


    topology_sort()
