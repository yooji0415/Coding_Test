def solution(number, k):
    n_list = list(number)
    stack = []
    for n in n_list:
        if not stack or k == 0:
            stack.append(n)
        else:
            while stack and int(stack[-1]) < int(n):
                stack.pop()
                k -= 1
                if k == 0:
                    break

            stack.append(n)

    while k > 0:
        stack.pop()
        k -= 1

    return "".join(stack)