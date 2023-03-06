n = int(input())

works = []
for _ in range(n):
    time, price = map(int, input().split())
    works.append((time, price))

dp = [0 for _ in range(n + 1)]
for day in range(n - 1, -1, -1):
    time, price = works[day]
    if day + time > n:
        dp[day] = dp[day + 1]
        continue

    dp[day] = max(dp[day + 1], dp[day + time] + price)

print(dp[0])
