import sys

input = sys.stdin.readline

n, k = map(int, input().split())

idx = 0
array = [i for i in range(1, n + 1)]
answer = []

while array:
    idx += k - 1
    idx %= len(array)
    answer.append(str(array[idx]))
    del array[idx]

print("<" + ", ".join(answer) + ">")
