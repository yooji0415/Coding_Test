n = int(input())
array = [(0, 0)]
for _ in range(n):
    array.append(tuple(map(int, input().split())))

dp = [0] * (n + 2)
max_result = 0
# print(array)

for i in range(n, 0, -1):
    ti, pi = array[i]
    if i + ti > n + 1:
        dp[i] = max_result
        continue

    result = pi + dp[i + ti]
    if result > max_result:
        max_result = result

    dp[i] = max_result

print(dp[1])
print(dp)
