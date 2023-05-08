G = int(input())
P = int(input())

parents = [i for i in range(G + 1)]


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


cnt = 0
flag = True
for _ in range(P):
    gate = find_parents(int(input()), parents)
    if not flag:
        continue
    if gate == 0:
        flag = False
        continue
    union(gate, gate - 1, parents)
    cnt += 1

print(cnt)
