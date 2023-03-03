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
parents = [i for i in range(n + 1)]
for i in range(n):
    arr = list(map(int, input().split()))
    for j in range(len(arr)):
        if arr[j] == 1:
            union(parents, i + 1, j + 1)

course = list(map(int, input().split()))
first_parents = parents[course[0]]
flag = True
for i in range(1, m):
    if first_parents != parents[course[i]]:
        flag = False
        break

print(parents)
print("YES" if flag else "NO")
