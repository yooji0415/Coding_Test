import sys

n, k = map(int, sys.stdin.readline().split())
coins = []
for _ in range(n):
    coins.append(int(sys.stdin.readline()))

cnt = 0
for i in range(n - 1, -1, -1):
    cnt += k // coins[i]
    k %= coins[i]

print(cnt)