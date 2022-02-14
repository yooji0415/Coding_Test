import sys

n, m = map(int, sys.stdin.readline().split())
poketmon = {}
for i in range(1, n+1):
    name = sys.stdin.readline().strip()
    poketmon[i] = name

reverse_poketmon = dict(map(reversed, poketmon.items()))
for _ in range(m):
    search = sys.stdin.readline().strip()
    if search.isdigit():
        print(poketmon[int(search)])
    else:
        print(reverse_poketmon[search])
