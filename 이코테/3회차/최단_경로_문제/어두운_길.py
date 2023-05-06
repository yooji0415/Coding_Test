import heapq

N, M = map(int, input().split())
q = []
parents = [i for i in range(N)]


def find_parents(a, parents):
    if a != parents[a]:
        parents[a] = find_parents(parents[a], parents)
    return parents[a]


def union(a, b, parents):
    a = find_parents(a, parents)
    b = find_parents(b, parents)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b


total = 0
for _ in range(M):
    a, b, cost = map(int, input().split())
    total += cost
    heapq.heappush(q, (cost, a, b))

answer = 0
while q:
    cost, a, b = heapq.heappop(q)
    if find_parents(a, parents) != find_parents(b, parents):
        union(a, b, parents)
        answer += cost

print(total - answer)
