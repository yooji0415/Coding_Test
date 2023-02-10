import sys

input = sys.stdin.readline

g = int(input())
p = int(input())

planes = []
for _ in range(p):
    planes.append(int(input()))

parents = [i for i in range(g + 1)]


def find_parent(a):
    if parents[a] != a:
        parents[a] = find_parent(parents[a])
    return parents[a]


def union(a, b):
    a = find_parent(a)
    b = find_parent(b)

    if a < b:
        parents[b] = a
    else:
        parents[a] = b


cnt = 0
for p in planes:
    p_parent = find_parent(p)
    if p_parent == 0:
        break
    union(p_parent - 1, p_parent)
    cnt += 1

print(cnt)
