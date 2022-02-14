import sys
from itertools import permutations

n, m = map(int, sys.stdin.readline().split())
input_list = list(map(int, sys.stdin.readline().split()))
input_list.sort()
answer = list(permutations(input_list, m))
for a in answer:
    ans = ""
    for b in a:
        ans += str(b) + " "

    print(ans)
