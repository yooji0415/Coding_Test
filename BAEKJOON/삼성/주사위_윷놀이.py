dice = list(map(int, input().split()))

graph = [[1], [2], [3], [4], [5], [6, 21], [7], [8], [9], [10], [11, 25], [12], [13], [14], [15], [16, 27],
         [17], [18], [19], [20], [32], [22], [23], [24], [30], [26], [24], [28], [29], [24], [31], [20], [32]]
score = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 13, 16, 19, 25, 22, 24, 28, 27, 26, 30, 35, 0]
horses = [0, 0, 0, 0]
answer = 0


def backtracking(loc, horses, result):
    global answer
    if loc >= 10:
        answer = max(answer, result)
        return

    for i in range(4):
        x = horses[i]
        if len(graph[x]) == 2:
            x = graph[x][1]
        else:
            x = graph[x][0]
        for j in range(1, dice[loc]):
            x = graph[x][0]
        if x == 32 or (x < 32 and x not in horses):
            before = horses[i]
            horses[i] = x
            backtracking(loc + 1, horses, result + score[x])
            horses[i] = before
    return


backtracking(0, horses, 0)
print(answer)
