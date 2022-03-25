def solution(priorities, location):
    q = []
    cnt = 0
    for i in range(len(priorities)):
        q.append([priorities[i], i])

    while q:
        p = q[0][0]
        idx = 0
        for i in range(len(q)):
            if p < q[i][0]:
                p = q[i][0]
                idx = i
        q = q[idx:] + q[:idx]
        item = q.pop(0)
        cnt += 1
        if item[1] == location:
            return cnt


# 모범답안
# any를 이용한 참신한 풀이
def best_solution(priorities, location):
    queue =  [(i,p) for i,p in enumerate(priorities)]
    answer = 0
    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer
            