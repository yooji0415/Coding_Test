import sys
from collections import deque

input = sys.stdin.readline

tc = int(input())
for _ in range(tc):
    commands = list(input().strip())
    n = int(input())
    line = []
    if n == 0:
        input()
        line = deque([])
    else:
        line = list(map(int, input().strip()[1:-1].split(",")))
        line = deque(line)

    is_reverse = False
    flag = True
    for command in commands:
        if command == "R":
            is_reverse = False if is_reverse else True
        if command == "D":
            if len(line) < 1:
                flag = False
                break
            if is_reverse:
                line.pop()
            else:
                line.popleft()

    if not flag:
        print("error")
        continue
    if is_reverse:
        line = list(map(str, reversed(list(line))))
    else:
        line = list(map(str, list(line)))
    print("[" + ",".join(line) + "]")
