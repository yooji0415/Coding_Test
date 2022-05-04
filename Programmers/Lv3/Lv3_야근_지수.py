import heapq


def solution(n, works):
    heap = []
    for i in works:
        heapq.heappush(heap, -i)

    for _ in range(n):
        if heap[0] == 0:
            break

        temp = heapq.heappop(heap)
        temp += 1
        heapq.heappush(heap, temp)

    answer = 0
    for i in heap:
        answer += i ** 2

    return answer