import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())

if k < n:
    print(n-k)
    exit(0)

queue = deque()
queue.append(n)
finish = {
    n: 0
}
while k not in finish:
        num = queue.popleft()
        if 100000 >= num+1 and num+1 not in finish:
            finish[num+1] = finish[num] + 1
            queue.append(num+1)
        if 100000 >= num*2 and num*2 not in finish:
            finish[num*2] = finish[num] + 1
            queue.append(num*2)
        if 0 <= num-1 and num-1 not in finish:
            finish[num-1] = finish[num] + 1
            queue.append(num-1)

print(finish[k])
