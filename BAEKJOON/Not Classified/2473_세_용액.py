import sys

input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))

array.sort()
best = int(1e9) * 3
answer = [0, 0, 0]

for i in range(n - 2):
    start = i + 1
    end = n - 1
    while start < end:
        result = array[i] + array[start] + array[end]
        if abs(result) < best:
            best = abs(result)
            answer = [array[i], array[start], array[end]]
        if result < 0:
            start += 1
        elif result > 0:
            end -= 1
        else:
            break

print(answer[0], answer[1], answer[2])
