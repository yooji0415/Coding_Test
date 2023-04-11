N = int(input())
array = list(map(int, input().split()))
operator = list(map(int, input().split()))
total_operator = sum(operator)
max_val = -int(1e9)
min_val = int(1e9)


def dfs(array, operator, cnt, val):
    global max_val
    global min_val
    if cnt == total_operator:
        max_val = max(max_val, val)
        min_val = min(min_val, val)
        return

    if operator[0] > 0:
        operator[0] -= 1
        dfs(array, operator, cnt + 1, val + array[cnt + 1])
        operator[0] += 1

    if operator[1] > 0:
        operator[1] -= 1
        dfs(array, operator, cnt + 1, val - array[cnt + 1])
        operator[1] += 1

    if operator[2] > 0:
        operator[2] -= 1
        dfs(array, operator, cnt + 1, val * array[cnt + 1])
        operator[2] += 1

    if operator[3] > 0:
        operator[3] -= 1
        dfs(array, operator, cnt + 1, int(val / array[cnt + 1]))
        operator[3] += 1


dfs(array, operator, 0, array[0])
print(max_val)
print(min_val)
