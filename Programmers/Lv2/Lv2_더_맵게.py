import heapq


def solution(scoville, K):
    heapq.heapify(scoville)
    cnt = 0

    while scoville[0] < K:
        if len(scoville) > 1:
            f = heapq.heappop(scoville)
            s = heapq.heappop(scoville)
            n = f + s * 2
            heapq.heappush(scoville, n)
            cnt += 1
        else:
            return -1

    return cnt

