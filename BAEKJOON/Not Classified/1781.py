import sys
import heapq

n = int(sys.stdin.readline())
array = []
q = []

for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    array.append((a, b))

array.sort()

for i in array:
    a = i[0]
    heapq.heappush(q, i[1])
    if a < len(q):
        heapq.heappop(q)

print(sum(q))
