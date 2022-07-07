import sys
from collections import deque


tc = int(sys.stdin.readline())
for _ in range(tc):
    input_line = sys.stdin.readline().strip()
    input_list = list(input_line)
    left = deque()
    right = deque()
    for key in input_list:
        if key == '<':
            if left:
                temp = left.pop()
                right.appendleft(temp)
        elif key == '>':
            if right:
                temp = right.popleft()
                left.append(temp)
        elif key == '-':
            if left:
                left.pop()
        else:
            left.append(key)

    for l in left:
        print(l, end='')
    for r in right:
        print(r, end='')
    print()
