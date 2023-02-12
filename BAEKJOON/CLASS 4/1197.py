import sys

input = sys.stdin.readline

def find_parent(parents, a):
    if parents[a] != a:
        parents[a] = find_parent(parents, parents[a])

    return parents[a]


def union(parents, a, b):
    a = find_parent(parents, a)
    b = find_parent(parents, b)

    if a < b:
        parents[b] = a
    else:
        parents[a] = b


v, e = map(int, input().split())
parents = [i for i in range(v + 1)]

edges = []
result = 0

for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()

for edge in edges:
    cost, a, b = edge
    if find_parent(parents, a) != find_parent(parents, b):
        union(parents, a, b)
        result += cost

print(result)
