import sys

input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))
stack = []
answer = [-1] * n

for i in range(n):
    while stack and stack[-1][0] < array[i]:
        val, idx = stack.pop()
        answer[idx] = array[i]

    stack.append((array[i], i))

print(" ".join(list(map(str, answer))))
