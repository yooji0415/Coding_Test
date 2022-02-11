import sys
from collections import deque

n = int(sys.stdin.readline())
tree = {i: [] for i in range(n + 1)}

for _ in range(n - 1):
    s, e, v = map(int, sys.stdin.readline().split())
    tree[s].append([e, v])
    tree[e].append([s, v])


def bfs(s):
    q = deque()
    q.append([s, 0])
    v = [False] * (n + 1)
    v[s] = True
    result = [0, 0]
    while q:
        now, cnt = q.popleft()
        for i in tree[now]:
            next_num, value = i[0], i[1]
            if not v[next_num]:
                v[next_num] = True
                q.append([next_num, cnt + value])
                if result[1] < cnt + value:
                    result[0] = next_num
                    result[1] = cnt + value

    return result


first_try = bfs(1)
answer = bfs(first_try[0])
print(answer[1])
