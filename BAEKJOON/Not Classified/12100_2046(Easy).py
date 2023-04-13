import sys
from collections import deque
import copy

input = sys.stdin.readline

n = int(input())
graph = []
answer = 0

for _ in range(n):
    graph.append(list(map(int, input().split())))


def move_left(graph):
    result = []
    for line in graph:
        stack = []
        for y in range(len(line)):
            num = line[y]
            if num == 0:
                continue
            if not stack:
                stack.append((num, False))
                continue
            flag = True
            if stack and not stack[-1][1] and stack[-1][0] == num:
                num *= 2
                flag = False
                stack.pop()
            if flag:
                stack.append((num, False))
            else:
                stack.append((num, True))
        while len(stack) < len(line):
            stack.append((0, False))
        stack = [x[0] for x in stack]
        result.append(stack)
    return result


def move_right(graph):
    result = []
    for line in graph:
        stack = deque()
        for y in range(len(line) - 1, -1, -1):
            num = line[y]
            if num == 0:
                continue
            if not stack:
                stack.appendleft((num, False))
                continue
            flag = True
            if stack and not stack[0][1] and stack[0][0] == num:
                num *= 2
                flag = False
                stack.popleft()
            if flag:
                stack.appendleft((num, False))
            else:
                stack.appendleft((num, True))
        while len(stack) < len(line):
            stack.appendleft((0, False))
        stack = [x[0] for x in stack]
        result.append(list(stack))
    return result


def move_up(graph):
    result = [[0] * len(graph) for _ in range(len(graph))]
    for y in range(len(graph)):
        line = []
        for x in range(len(graph)):
            line.append(graph[x][y])

        stack = []
        for idx in range(len(line)):
            num = line[idx]
            if num == 0:
                continue
            if not stack:
                stack.append((num, False))
                continue
            flag = True
            if stack and not stack[-1][1] and stack[-1][0] == num:
                num *= 2
                flag = False
                stack.pop()
            if flag:
                stack.append((num, False))
            else:
                stack.append((num, True))
        while len(stack) < len(line):
            stack.append((0, False))

        for x in range(len(graph)):
            result[x][y] = stack[x][0]
    return result


def move_down(graph):
    result = [[0] * len(graph) for _ in range(len(graph))]
    for y in range(len(graph)):
        line = []
        for x in range(len(graph)):
            line.append(graph[x][y])

        stack = deque()
        for idx in range(len(line) - 1, -1, -1):
            num = line[idx]
            if num == 0:
                continue
            if not stack:
                stack.appendleft((num, False))
                continue
            flag = True
            if stack and not stack[0][1] and stack[0][0] == num:
                num *= 2
                flag = False
                stack.popleft()
            if flag:
                stack.appendleft((num, False))
            else:
                stack.appendleft((num, True))
        while len(stack) < len(line):
            stack.appendleft((0, False))

        for x in range(len(graph)):
            result[x][y] = stack[x][0]
    return result


def dfs(cnt, graph):
    global answer
    if cnt == 5:
        result = 0
        for x in range(len(graph)):
            for y in range(len(graph)):
                if result < graph[x][y]:
                    result = graph[x][y]

        answer = max(answer, result)
        return

    dfs(cnt + 1, move_up(graph))
    dfs(cnt + 1, move_right(graph))
    dfs(cnt + 1, move_down(graph))
    dfs(cnt + 1, move_left(graph))


dfs(0, graph)
print(answer)
