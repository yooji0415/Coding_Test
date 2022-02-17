def solution(s):
    stack = []
    for l in s:
        if not stack:
            stack.append(l)
        else:
            if stack[-1] == l:
                stack.pop()
            else:
                stack.append(l)

    if stack:
        return 0
    else:
        return 1
