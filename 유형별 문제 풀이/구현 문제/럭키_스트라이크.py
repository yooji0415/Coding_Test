nums = list(map(int, list(input())))
length = len(nums)
split_point = length // 2

a_part = sum(nums[0:split_point])
b_part = sum(nums[split_point:])

print('LUCKY' if a_part == b_part else 'READY')
