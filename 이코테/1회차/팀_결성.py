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

for _ in range(m):
    t, a, b = map(int, input().split())

    if t == 0:
        union(parents, a, b)
        continue

    a = find_parents(parents, a)
    b = find_parents(parents, b)

    print('NO' if a != b else 'YES')

