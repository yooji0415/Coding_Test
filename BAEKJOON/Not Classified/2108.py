import sys


N = int(sys.stdin.readline().strip())
data = []
data_cnt = {}
min_num = 4001
max_num = -4001
data_sum = 0
for _ in range(N):
    temp = int(sys.stdin.readline().strip())
    data.append(temp)
    data_sum += temp
    if temp < min_num:
        min_num = temp
    if max_num < temp:
        max_num = temp
    if temp not in data_cnt:
        data_cnt[temp] = 1
    else:
        data_cnt[temp] += 1

data.sort()
sorted_cnt = sorted(data_cnt.items(), key=lambda item: item[1], reverse=True)
most_data = sorted_cnt[0][0]
center_idx = N // 2

print(round(data_sum/N))
print(data[center_idx])
print(most_data)
print(max_num - min_num)
