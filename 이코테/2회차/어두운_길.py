import heapq


def find_parents(parents, a):
    if parents[a] != a:
        parents[a] = find_parents(parents, parents[a])
    return parents[a]


def union(parents, a, b):
    a = find_parents(parents, a)
    b = find_parents(parents, b)

    if a < b:
        parents[b] = a
    else:
        parents[a] = b


n, m = map(int, input().split())

parents = [i for i in range(n)]
q = []
total_cost = 0
for _ in range(m):
    a, b, cost = map(int, input().split())
    total_cost += cost
    heapq.heappush(q, (cost, a, b))

remain_cost = 0
while q:
    cost, a, b = heapq.heappop(q)
    parents_a = find_parents(parents, a)
    parents_b = find_parents(parents, b)

    if parents_a == parents_b:
        continue

    remain_cost += cost
    union(parents, a, b)

print(total_cost - remain_cost)