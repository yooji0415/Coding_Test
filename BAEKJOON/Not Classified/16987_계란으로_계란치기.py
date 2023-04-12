import sys

input = sys.stdin.readline

n = int(input())
eggs = []
for _ in range(n):
    s, w = map(int, input().split())
    eggs.append([s, w])

answer = 0


def dfs(idx, eggs, n):
    global answer
    if idx == n:
        result = 0
        for egg in eggs:
            if egg[0] <= 0:
                result += 1
        answer = max(answer, result)
        return

    if eggs[idx][0] <= 0:
        dfs(idx + 1, eggs, n)
        return

    flag = True
    for i in range(n):
        if i == idx:
            continue
        next_s, next_w = eggs[i]
        if next_s > 0:
            flag = False
            now_s, now_w = eggs[idx]
            eggs[idx] = [now_s - next_w, now_w]
            eggs[i] = [next_s - now_w, next_w]

            dfs(idx + 1, eggs, n)

            eggs[idx] = [now_s, now_w]
            eggs[i] = [next_s, next_w]

    if flag:
        dfs(idx + 1, eggs, n)


dfs(0, eggs, n)
print(answer)
