N = int(input())
planets = []
parents = [i for i in range(N)]
for _ in range(N):
    x, y, z = map(int, input().split())
    planets.append((x, y, z))

edges = []
for a in range(1, N):
    for b in range(0, a):
        ax, ay, az = planets[a]
        bx, by, bz = planets[b]
        edges.append((abs(ax - bx), a, b))
        edges.append((abs(ay - by), a, b))
        edges.append((abs(az - bz), a, b))


def find_parents(a, parents):
    if a != parents[a]:
        parents[a] = find_parents(parents[a], parents)
    return parents[a]


def untion(a, b, parents):
    a = find_parents(a, parents)
    b = find_parents(b, parents)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b


edges.sort(reverse=True)
answer = 0
while edges:
    cost, a, b = edges.pop()
    if find_parents(a, parents) != find_parents(b, parents):
        untion(a, b, parents)
        answer += cost

print(answer)
