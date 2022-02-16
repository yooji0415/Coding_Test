from collections import deque as dq


def solution(progresses, speeds):
    pr = dq(progresses)
    sp = dq(speeds)
    answer = []

    while pr:
        cnt = 0
        for i in range(len(sp)):
            pr[i] += sp[i]

        while pr and pr[0] >= 100:
            pr.popleft()
            sp.popleft()
            cnt += 1

        if cnt != 0:
            answer.append(cnt)

    return answer


# 모범답안
# 모든 원소를 돌면서 덧셈 처리해준 것이 아니라
# 시간이라는 요소를 사용해서 이를 카운팅 하는 방법을 사용했다
def solution(progresses, speeds):
    print(progresses)
    print(speeds)
    answer = []
    time = 0
    count = 0
    while len(progresses)> 0:
        if (progresses[0] + time*speeds[0]) >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        else:
            if count > 0:
                answer.append(count)
                count = 0
            time += 1
    answer.append(count)
    return answer
