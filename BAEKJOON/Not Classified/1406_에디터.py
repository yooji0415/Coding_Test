import sys
from collections import deque

input = sys.stdin.readline

default = input().strip()

left = deque(list(default))
right = deque([])

m = int(input())
for i in range(m):
    line = input().strip()
    if len(line) == 1:
        if line == "L":
            if len(left) == 0:
                continue
            right.appendleft(left.pop())
        elif line == "D":
            if len(right) == 0:
                continue
            left.append(right.popleft())
        else:
            if len(left) == 0:
                continue
            left.pop()
    else:
        command, alpha = line.split(" ")
        left.append(alpha)

print("".join(list(left)) + "".join(list(right)))
