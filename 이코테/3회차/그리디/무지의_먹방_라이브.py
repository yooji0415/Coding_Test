from heapq import heappop, heappush


def solution(food_times, k):
    # 모든 음식을 다 먹어도 시간이 남거나 맞는 경우
    if sum(food_times) <= k:
        return -1

    # 어떤 아이디어로 하면 될 것인가
    # 남은 음식 중에서 가장 시간이 덜 걸리는 음식을 고른다.
    # 해당 음식 시간 * 총 음식 수 = 그 음식이 사라지는 순간

    # 음식을 우선순위 큐에 저장한다.
    # 넣을 때는 (음식 시간, 인덱스)
    q = []
    for i in range(len(food_times)):
        heappush(q, (food_times[i], i + 1))

    # 사이클을 돌면서 더한 시간
    total_time = 0
    # 사이클에 남은 음식 수
    remain_foods = len(food_times)
    # 사이클을 돈 횟수
    cycle = 0

    # 이제 언제까지 도느냐
    # (q[0][0] - cycle) * remain_foods >= k - total_time
    # 드가보자
    while q and (q[0][0] - cycle) * remain_foods <= k - total_time:
        time, idx = heappop(q)
        total_time += (time - cycle) * remain_foods
        cycle = time
        remain_foods -= 1

    # 이제 남은 시간 순으로 인덱스를 찾으면 된다.
    q.sort(key=lambda x: x[1])
    remain_time = k - total_time
    return q[remain_time % len(q)][1]


print(solution([3, 1, 2], 5))
