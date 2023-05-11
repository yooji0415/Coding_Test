N, M = map(int, input().split())
graph = []


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


parents = [i for i in range(N + 1)]
for a in range(1, N + 1):
    array = list(map(int, input().split()))
    for b in range(1, N + 1):
        if array[b - 1] == 1:
            union(a, b, parents)

test = list(map(int, input().split()))
test_parents = parents[test[0]]
answer = True
for num in test[1:]:
    if parents[num] != test_parents:
        answer = False
        break

print("YES" if answer else "NO")
