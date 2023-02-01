n, m, k = map(int, input().split(" "))
numbers = list(map(int, input().split(" ")))
numbers.sort(reverse=True)

answer = 0
for i in range(m):
    if i != 0 and i % k == 0:
        answer += numbers[1]
        continue
    answer += numbers[0]

print(answer)
