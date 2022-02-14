import sys


def bfs(grape, n, node, start):
    queue = []
    queue.append(start)
    while queue:
        p = queue.pop(0)
        for i in grape[p]:
            if node[i] == 0:
                node[i] = 1
                queue.append(i)


n, m = map(int, sys.stdin.readline().split())
grape = [[] for row in range(n + 1)]

for _ in range(m):
    p1, p2 = map(int, sys.stdin.readline().split())
    grape[p1].append(p2)
    grape[p2].append(p1)

cnt = 0
node = [0 for _ in range(n+1)]
for i in range(1, n+1):
    if node[i] == 0:
        bfs(grape, n, node, i)
        cnt += 1

print(cnt)
