# -*- coding: utf-8 -*-
def solution(prices):
    answer = [0] * len(prices)
    stack = []
    for i, p in enumerate(prices):
        # 초기에 스택이 비었을 경우
        if not stack:
            stack.append([p, i])
        # 스택에 값이 있을 경우
        else:
            # 비교 값 보다 큰 값들을 스택에서 빼고 기간을 입력해준다
            while stack and stack[-1][0] > p:
                temp = stack.pop()
                answer[temp[1]] = i - temp[1]

            # 다 정리된 이후에는 값을 스택에 넣어준다
            stack.append([p, i])

    # for문을 다 돌았으나 스택에 값이 남아있을 경우 이를 처리한다
    while stack:
        temp = stack.pop()
        answer[temp[1]] = len(prices) - 1 - temp[1]

    return answer
