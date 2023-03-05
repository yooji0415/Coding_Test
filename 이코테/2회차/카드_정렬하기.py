import sys
import heapq


input = sys.stdin.readline

n = int(input())
nums = []

for _ in range(n):
    heapq.heappush(nums, int(input()))

answer = 0
while len(nums) > 1:
    first = heapq.heappop(nums)
    second = heapq.heappop(nums)
    answer += first + second
    heapq.heappush(nums, first + second)

print(answer)
