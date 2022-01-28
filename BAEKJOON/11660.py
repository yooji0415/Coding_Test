import sys

n, m = map(int, sys.stdin.readline().split())
num = []
for _ in range(n):
    num.append(list(map(int, sys.stdin.readline().split())))

for j in range(n):
    for i in range(n):
        if i == 0 and j == 0:
            continue
        elif i == 0:
            num[i][j] += num[i][j-1]
        elif j == 0:
            num[i][j] += num[i-1][j]
        else:
            num[i][j] += num[i-1][j] + num[i][j-1] - num[i-1][j-1]

# print(num)
for _ in range(m):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    if x1 == 1 and y1 == 1:
        print(num[x2-1][y2-1])
    elif x1 == 1:
        print(num[x2-1][y2-1] - num[x2-1][y1-2])
    elif y1 == 1:
        print(num[x2-1][y2-1] - num[x1-2][y2-1])
    else:
        print(num[x2-1][y2-1] + num[x1-2][y1-2] - num[x2-1][y1-2] - num[x1-2][y2-1])
