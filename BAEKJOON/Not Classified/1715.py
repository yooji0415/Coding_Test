import heapq
import sys


n = int(sys.stdin.readline())
heap = []
for _ in range(n):
    heapq.heappush(heap, int(sys.stdin.readline()))

answer = 0
while len(heap) != 1:
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)
    c = a + b
    answer += c
    heapq.heappush(heap, c)

print(answer)
    