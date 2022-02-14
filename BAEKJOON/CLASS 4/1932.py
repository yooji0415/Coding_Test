import sys

n = int(sys.stdin.readline())
tri = []
for i in range(n):
    tri.append(list(map(int, sys.stdin.readline().split())))

line = 2
for i in range(1, n):
    for j in range(line):
        if j == 0:
            tri[i][j] += tri[i-1][j]
        elif i == j:
            tri[i][j] += tri[i-1][j-1]
        else:
            tri[i][j] += max(tri[i-1][j-1], tri[i-1][j])
    line += 1

print(max(tri[n-1]))
