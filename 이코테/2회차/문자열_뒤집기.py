nums = list(map(int, list(input())))

zero_cnt = 0
one_cnt = 0
now = nums[0]
for num in nums:
    if num == now:
        continue
    else:
        if now == 1:
            one_cnt += 1
        else:
            zero_cnt += 1
        now = num

if now == 1:
    one_cnt += 1
else:
    zero_cnt += 1

print(zero_cnt if one_cnt > zero_cnt else one_cnt)
