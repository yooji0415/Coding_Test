import sys

n = int(sys.stdin.readline())
num = []
for _ in range(n):
    num.append(list(map(int, sys.stdin.readline().split())))

num.sort(key=lambda x: (x[0], x[1]))
for item in num:
    print("{} {}".format(item[0], item[1]))
