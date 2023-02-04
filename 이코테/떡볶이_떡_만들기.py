import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
items = list(map(int, sys.stdin.readline().rstrip().split()))

start = 0
end = max(items)
answer = 0

while start <= end:
    mid = (start + end) // 2
    total = 0
    for item in items:
        if item > mid:
            total += item - mid

    if total < m:
        end = mid - 1
    else:
        answer = mid
        start = mid + 1

print(answer)
