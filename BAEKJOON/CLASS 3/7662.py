import sys
import heapq

t = int(sys.stdin.readline())
for _ in range(t):
    k = int(sys.stdin.readline())
    heap_max = []
    heap_min = []
    visited = [False] * k
    for i in range(k):
        a, b = map(str, sys.stdin.readline().split())
        if a == "I":
            heapq.heappush(heap_max, (-int(b), i))
            heapq.heappush(heap_min, (int(b), i))
            visited[i] = True
        else:
            if b == "1":
                while heap_max and visited[heap_max[0][1]] == False:
                    heapq.heappop(heap_max)

                if heap_max:
                    visited[heap_max[0][1]] = False
                    heapq.heappop(heap_max)

            else:
                while heap_min and visited[heap_min[0][1]] == False:
                    heapq.heappop(heap_min)

                if heap_min:
                    visited[heap_min[0][1]] = False
                    heapq.heappop(heap_min)

    if True not in visited:
        print("EMPTY")
    else:
        while heap_max and visited[heap_max[0][1]] == False:
            heapq.heappop(heap_max)
        while heap_min and visited[heap_min[0][1]] == False:
            heapq.heappop(heap_min)

        print(-heap_max[0][0], heap_min[0][0])