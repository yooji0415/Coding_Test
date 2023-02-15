import sys
from itertools import combinations_with_replacement

n, m = map(int, input().split())
arr = list(set(map(int, input().split())))
arr.sort()

for combi in combinations_with_replacement(arr, m):
    print(" ".join(list(map(str, combi))))
