n, m = map(int, input().split())
parents = [i for i in range(n + 1)]


def find_parent(num):
    if parents[num] != num:
        parents[num] = find_parent(parents[num])
    return parents[num]


def union(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b


for i in range(1, n + 1):
    connects = list(map(int, input().split()))
    for j in range(n):
        if connects[j] == 1:
            union(i, j + 1)

line = list(map(int, input().split()))
target = parents[line[0]]
flag = True
for i in range(1, len(line)):
    if find_parent(line[i]) != target:
        flag = False
        break

if flag:
    print("YES")
else:
    print("NO")
