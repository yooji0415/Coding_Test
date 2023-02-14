import heapq
import sys

input = sys.stdin.readline

n, k = map(int, input().split())
answer = 0
jewels = []
bags = []

for _ in range(n):
    weight, value = map(int, input().split())
    heapq.heappush(jewels, (weight, value))

for _ in range(k):
    weight = int(input())
    bags.append(weight)

bags.sort()

temp = []
for bag in bags:
    while jewels and bag >= jewels[0][0]:
        heapq.heappush(temp, -heapq.heappop(jewels)[1])
    if temp:
        answer -= heapq.heappop(temp)
    elif not jewels:
        break

print(answer)
