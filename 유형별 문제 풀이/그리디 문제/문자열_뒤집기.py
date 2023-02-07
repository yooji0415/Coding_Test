n = list(map(int, list(input())))

zero_cnt = 0
one_cnt = 0

start = -1
for i in range(len(n)):
    if start == -1:
        start = n[i]
        continue

    if n[i] != start:
        if start == 1:
            one_cnt += 1
        else:
            zero_cnt += 1
        start = n[i]

if start == 1:
    one_cnt += 1
else:
    zero_cnt += 1

# print(f"one: {one_cnt} zero: {zero_cnt}")
print(min(one_cnt, zero_cnt))
