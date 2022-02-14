n, k = map(int, input().split())
result_list = []
for i in range(0, 11):
    if i == 0 or i == 1:
        result_list.append(i)
    else:
        result_list.append(result_list[-1] * i)

if k == 0 or n == k:
    print(1)
else:
    print(result_list[n] // (result_list[k] * result_list[n-k]))