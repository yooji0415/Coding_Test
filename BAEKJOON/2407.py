import sys

n, m = map(int, sys.stdin.readline().split())

sum = 1
for i in range(n, n-m, -1):
    sum *= i

for j in range(1, m+1):
    sum = sum // j

print(int(sum))
