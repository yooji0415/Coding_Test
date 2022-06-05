import sys
from collections import deque


s = list(sys.stdin.readline().strip())
queue = deque()
switch = False
special = ""
normal = deque()
for alpha in s:
    if alpha == '<':
        if normal:
            queue.append(''.join(normal))
            normal = deque()

        special += alpha
        switch = True
    elif alpha == '>':
        special += alpha
        switch = False
        queue.append(special)
        special = ""
    else:
        if switch:
            special += alpha
        else:
            if alpha == ' ':
                queue.append(''.join(normal))
                normal = deque()
                queue.append(alpha)
            else:
                normal.appendleft(alpha)

if normal != "":
    queue.append(''.join(normal))

answer = ""
while queue:
    answer += queue.popleft()

print(answer)
