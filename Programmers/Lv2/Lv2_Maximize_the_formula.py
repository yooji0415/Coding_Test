from itertools import permutations
from collections import deque


def cal(n1, n2, o):
    if o == "*":
        return str(int(n1) * int(n2))
    elif o == "+":
        return str(int(n1) + int(n2))
    else:
        return str(int(n1) - int(n2))


def test(e, oper):
    q = deque(e)
    for o in oper:
        stack = []
        while q:
            temp = q.popleft()
            if temp == o:
                oResult = cal(stack.pop(), q.popleft(), o)
                stack.append(oResult)
            else:
                stack.append(temp)

        q = deque(stack)

    return q[0]


def solution(expression):
    # 우선 숫자와 연산자를 구분해서 넣어둔다.
    n = ""
    e = []
    for l in expression:
        if l.isdigit():
            n += l
        else:
            e.append(n)
            e.append(l)
            n = ""

    e.append(n)

    # 이후 모든 경우에서 테스트를 진행해본다.
    answer = []
    operList = list(permutations(["*", "+", "-"], 3))
    for oper in operList:
        result = test(e, oper)
        answer.append(abs(int(result)))

    return max(answer)

