from collections import deque


def solution(cap, n, deliveries, pickups):
    d_q = deque(reversed(deliveries))
    p_q = deque(reversed(pickups))

    answer = 0
    while d_q and d_q[0] == 0:
        d_q.popleft()

    while p_q and p_q[0] == 0:
        p_q.popleft()

    while d_q or p_q:
        max_len = max(len(d_q), len(p_q))
        # print("--start--")
        # print(d_q)
        # print(p_q)
        # print("--end--")
        answer += max_len

        now_cap = cap
        while d_q and now_cap > 0:
            if d_q[0] == 0:
                d_q.popleft()
                continue

            if d_q[0] <= now_cap:
                now_cap -= d_q[0]
                d_q.popleft()

            else:
                d_q[0] -= now_cap
                break

        while d_q and d_q[0] == 0:
            d_q.popleft()

        # print(d_q)

        now_cap = cap
        while p_q and now_cap > 0:
            if p_q[0] == 0:
                p_q.popleft()
                continue

            if p_q[0] <= now_cap:
                now_cap -= p_q[0]
                p_q.popleft()
            else:
                p_q[0] -= now_cap
                break

        while p_q and p_q[0] == 0:
            p_q.popleft()

        # print(p_q)

    return answer * 2