nums = list(map(int, list(input())))

answer = nums[0]
for i in range(1, len(nums)):
    if answer == 0 or nums[i] == 0:
        answer += nums[i]
    else:
        answer *= nums[i]

print(answer)
