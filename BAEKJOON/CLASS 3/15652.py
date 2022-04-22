from itertools import combinations_with_replacement
import sys

N, M = list(map(int, sys.stdin.readline().split()))
arr = [x for x in range(1, N + 1)]
per_list = combinations_with_replacement(arr, M)
for per in per_list:
    answer = " ".join(list(map(str, per)))
    print(answer)
