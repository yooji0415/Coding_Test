import sys

n, m = map(int, sys.stdin.readline().split())
n_list = set()
for _ in range(n):
    name = sys.stdin.readline().strip()
    n_list.add(name)

cnt = set()
for _ in range(m):
    check = sys.stdin.readline().strip()
    cnt.add(check)

answer = sorted(list(n_list & cnt))
print(len(answer))
for person in answer:
    print(person)
