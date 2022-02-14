import sys

n = int(sys.stdin.readline())
time_list = list(map(int, sys.stdin.readline().split()))

time_list.sort()
result = 0
for i in range(n):
    result += (n-i) * time_list[i]

print(result)