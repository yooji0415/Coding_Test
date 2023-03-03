n = int(input())
houses = list(map(int, input().split()))

houses.sort()
answer = sum(houses)
point = 0

for i in range(len(houses)):
    now = houses[i]
    left_sum = sum(houses[:i])
    right_sum = sum(houses[i + 1:])
    left_result = now * i - left_sum
    right_result = right_sum - now * (n - 1 - i)
    result = left_result + right_result
    if answer > result:
        answer = result
        point = now

print(point)
