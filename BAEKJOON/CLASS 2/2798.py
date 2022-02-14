n, m = map(int, input().split())
n_list = list(map(int, input().split()))
result = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if m < n_list[i] + n_list[j] + n_list[k]:
                continue
            else:
                result = max(result, n_list[i] + n_list[j] + n_list[k])

print(result)