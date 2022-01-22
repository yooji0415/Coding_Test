import sys
from itertools import combinations

n, m = map(int, sys.stdin.readline().split())
answer = list(combinations([i for i in range(1, n+1)], m))
for a in answer:
    ans = ""
    for b in a:
        ans += str(b) + " "

    print(ans)
