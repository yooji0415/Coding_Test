import sys

n = int(sys.stdin.readline().strip())
grape = [[0 for col in range(n + 1)] for row in range(n + 1)]
edge = int(sys.stdin.readline().strip())
for _ in range(edge):
    p1, p2 = map(int, sys.stdin.readline().split())
    grape[p1][p2] = 1
    grape[p2][p1] = 1

queue = [1]
computer = []
while queue:
    c = queue.pop(0)
    if c not in computer:
        computer.append(c)
    for i in range(1, n+1):
        if grape[c][i] == 1 and i not in computer:
            queue.append(i)
            grape[c][i] = 0
            grape[i][c] = 0

print(len(computer) - 1)
