import sys

input = sys.stdin.readline

n = int(input())

max_dp = [0, 0, 0]
min_dp = [0, 0, 0]

for row in range(n):
    if row == 0:
        a, b, c = map(int, input().split())
        max_dp = [a, b, c]
        min_dp = [a, b, c]
        continue

    a, b, c = map(int, input().split())
    max_dp = [a + max(max_dp[0], max_dp[1]), b + max(max_dp), c + max(max_dp[1], max_dp[2])]
    min_dp = [a + min(min_dp[0], min_dp[1]), b + min(min_dp), c + min(min_dp[1], min_dp[2])]

print(f"{max(max_dp)} {min(min_dp)}")
