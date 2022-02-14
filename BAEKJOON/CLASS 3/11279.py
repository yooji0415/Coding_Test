import sys
import heapq

n = int(sys.stdin.readline())
max_heap = []
for _ in range(n):
    num = int(sys.stdin.readline())
    if num != 0:
        heapq.heappush(max_heap, (-num))
    else:
        try:
            print(-1 * heapq.heappop(max_heap))
        except:
            print(0)

