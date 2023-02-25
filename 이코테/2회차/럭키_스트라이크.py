nums = list(map(int, list(input())))

length = len(nums)
first_part = sum(nums[:length // 2])
second_part = sum(nums[length // 2:])

if first_part == second_part:
    print("LUCKY")
else:
    print("READY")
