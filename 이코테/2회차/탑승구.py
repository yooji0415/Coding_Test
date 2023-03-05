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


# 탑승구 수
g = int(input())
# 비행기 수
p = int(input())

parents = [i for i in range(g + 1)]
cnt = 0
flag = False
for _ in range(p):
    want = int(input())
    if flag:
        continue
    want_parents = find_parents(parents, want)
    if want_parents != 0:
        cnt += 1
        union(parents, want, want_parents - 1)
    else:
        flag = True
    print(parents)

print(cnt)
