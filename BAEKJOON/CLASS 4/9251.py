import sys

s1 = sys.stdin.readline().strip()
s2 = sys.stdin.readline().strip()
l1 = len(s1)
l2 = len(s2)

dp = [[0 for _ in range(l1+1)] for _ in range(l2+1)]

for p2 in range(1, l2+1):
    for p1 in range(1, l1+1):
        if s1[p1-1] == s2[p2-1]:
            dp[p2][p1] = dp[p2-1][p1-1] + 1
        else:
            dp[p2][p1] = max(dp[p2-1][p1], dp[p2][p1-1])

# for l in dp:
#     print(l)

print(dp[l2][l1])
