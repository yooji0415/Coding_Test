n = int(input())
coins = list(map(int, input().split()))

coins.sort()

answer = 1
for coin in coins:
    if answer >= coin:
        answer += coin
    else:
        break

print(answer)
