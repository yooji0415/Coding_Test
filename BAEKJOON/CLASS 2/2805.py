import sys


N, M = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))

start, end = 1, max(trees)

while start <= end:
    total = 0
    mid = (start + end) // 2
    for tree in trees:
        if tree > mid:
            total += tree - mid

    if total >= M:
        start = mid + 1
    else:
        end = mid - 1

print(end)