from collections import deque as dq


def solution(numbers, target):
    ans = dq()
    start = 0
    ans.append(start)
    for i in range(len(numbers)):
        for j in range(len(ans)):
            temp = ans.popleft()
            ans.append(temp + numbers[i])
            ans.append(temp - numbers[i])

    return ans.count(target)
