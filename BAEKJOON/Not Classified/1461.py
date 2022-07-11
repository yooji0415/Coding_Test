import sys
import heapq

pos = []
neg = []

n, m = map(int, sys.stdin.readline().split())
book_list = list(map(int, sys.stdin.readline().split()))

for book in book_list:
    if book < 0:
        heapq.heappush(neg, book)
    elif book > 0:
        heapq.heappush(pos, -book)

dists = []
flag = 0
dist = 0
while neg:
    if flag % m == 0:
        dists.append(-heapq.heappop(neg))
    else:
        heapq.heappop(neg)
    flag += 1

flag = 0
dist = 0
while pos:
    if flag % m == 0:
        dists.append(-heapq.heappop(pos))
    else:
        heapq.heappop(pos)
    flag += 1

answer = sum(dists) * 2 - max(dists)
print(answer)
