from collections import deque

a, b = map(int, input().split())
q = deque([(a, 1)])

flag = False
answer = 0
while q:
    now, cnt = q.popleft()
    if now == b:
        answer = cnt
        flag = True
        break

    if now * 2 <= b:
        q.append((now * 2, cnt + 1))

    if now * 10 + 1 <= b:
        q.append((now * 10 + 1, cnt + 1))

print(answer if flag else -1)
