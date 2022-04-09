def solution(s):
    answer = 0
    if len(s) % 2 == 1:
        return 0

    for _ in range(len(s)):
        stack = []
        is_ok = True
        for i in range(len(s)):
            if s[i] in ['(', '{', '[']:
                stack.append(s[i])
            else:
                if not stack:
                    is_ok = False
                    break

                if stack[-1] == '(' and s[i] == ')':
                    stack.pop()
                elif stack[-1] == '{' and s[i] == '}':
                    stack.pop()
                elif stack[-1] == '[' and s[i] == ']':
                    stack.pop()
                else:
                    is_ok = False
                    break

        if is_ok:
            if not stack:
                answer += 1
            else:
                return 0

        s = s[1:] + s[0]

    return answer