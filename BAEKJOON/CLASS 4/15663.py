from itertools import permutations

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

for per in sorted(list(set(permutations(arr, m)))):
    print(" ".join(map(str, per)))
