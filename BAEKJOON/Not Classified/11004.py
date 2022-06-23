import sys


N, K = map(int, sys.stdin.readline().split(" "))
n_list = list(map(int, sys.stdin.readline().split(" ")))
n_list.sort()
print(n_list[K - 1])
