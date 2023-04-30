array1 = [" "] + list(input())
array2 = [" "] + list(input())
COL = len(array1)
ROW = len(array2)

dp = [[0] * COL for _ in range(ROW)]
for y in range(1, COL):
    dp[0][y] = dp[0][y - 1] + 1
for x in range(1, ROW):
    dp[x][0] = dp[x - 1][0] + 1

for x in range(1, ROW):
    for y in range(1, COL):
        if array1[y] == array2[x]:
            dp[x][y] = dp[x - 1][y - 1]
        else:
            dp[x][y] = min(dp[x - 1][y], dp[x][y - 1], dp[x - 1][y - 1]) + 1

for line in dp:
    print(line)
