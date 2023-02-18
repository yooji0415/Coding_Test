import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline


def find_parents(parents, a):
    if parents[a] != a:
        parents[a] = find_parents(parents, parents[a])

    return parents[a]


def union(parents, a, b):
    a = find_parents(parents, a)
    b = find_parents(parents, b)

    if a < b:
        parents[a] = b
    else:
        parents[b] = a


n, m = map(int, input().split())
parents = [i for i in range(n)]

answer = 0
cnt = 0
flag = False
for _ in range(m):
    cnt += 1
    a, b = map(int, input().split())
    if flag:
        continue
    a_parents = find_parents(parents, a)
    b_parents = find_parents(parents, b)
    if a_parents == b_parents:
        flag = True
        answer = cnt

    union(parents, a, b)

print(answer)
