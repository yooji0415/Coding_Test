import sys
from itertools import permutations


n = int(sys.stdin.readline().strip())
n_list = [x for x in range(1, n+1)]
p_list = list(permutations(n_list, n))

p_in = tuple(map(int, sys.stdin.readline().split()))
idx = p_list.index(p_in)
if idx == 0:
    print(-1)
else:
    for num in p_list[idx - 1]:
        print(num, end=" ")
