def find_parents(parents, target):
    if parents[target] != target:
        parents[target] = find_parents(parents, parents[target])

    return parents[target]


def union(parents, a, b):
    a = find_parents(parents, a)
    b = find_parents(parents, b)

    if a < b:
        parents[b] = a
    else:
        parents[a] = b


n, m = map(int, input().split())

parents = [i for i in range(n + 1)]
edges = []
answer_edges = []

for _ in range(m):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()

for edge in edges:
    cost, a, b = edge

    a_parent = find_parents(parents, a)
    b_parent = find_parents(parents, b)

    if a_parent != b_parent:
        union(parents, a, b)
        answer_edges.append(cost)

answer_edges.pop()
print(sum(answer_edges))
