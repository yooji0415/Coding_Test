import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())

check = [0] * 100001
q = deque()
q.append([n, 0])

while q:
    temp = q.popleft()
    if temp[0] == k:
        print(temp[1])
        break
    for next in [temp[0] - 1, temp[0] + 1, 2 * temp[0]]:
        if 0 <= next <= 100000 and check[next] == 0:
            check[next] = 1
            if next in [temp[0]-1, temp[0]+1]:
                q.append([next, temp[1] + 1])
            if next == 2 * temp[0]:
                q.appendleft([next, temp[1]])
