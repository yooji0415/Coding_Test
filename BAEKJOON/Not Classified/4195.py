import sys


def find(x):
    if x == parent[x]:
        return x
    else:
        p = find(parent[x])
        parent[x] = p
        return parent[x]


def union(x, y):
    x = find(x)
    y = find(y)
    if x != y:
        parent[y] = x
        number[x] += number[y]


tc = int(sys.stdin.readline())
for _ in range(tc):
    parent = dict()
    number = dict()
    friends = int(sys.stdin.readline())
    for _ in range(friends):
        a, b = sys.stdin.readline().split()
        if a not in parent:
            parent[a] = a
            number[a] = 1
        if b not in parent:
            parent[b] = b
            number[b] = 1

        union(a, b)
        print(number[find(a)])
