import heapq


def solution(food_times, k):
    if sum(food_times) <= k:
        return -1

    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i + 1))

    spend_time = 0
    prev = 0
    length = len(food_times)

    while spend_time + (q[0][0] - prev) * length <= k:
        now = heapq.heappop(q)[0]
        spend_time += (now - prev) * length
        prev = now
        length -= 1

    q.sort(key=lambda x: x[1])

    return q[(k - spend_time) % length][1]