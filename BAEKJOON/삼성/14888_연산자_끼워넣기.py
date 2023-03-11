import sys

input = sys.stdin.readline

max_answer = -int(1e9)
min_answer = int(1e9)

N = int(input())

nums = list(map(int, input().split()))
commands = list(map(int, input().split()))


def back_tracking(temp_sum, num_idx):
    global commands
    global max_answer
    global min_answer

    if num_idx == len(nums) - 1:
        max_answer = max(temp_sum, max_answer)
        min_answer = min(temp_sum, min_answer)
        return

    for i in range(4):
        if commands[i] == 0:
            continue

        commands[i] -= 1
        if i == 0:
            back_tracking(temp_sum + nums[num_idx + 1], num_idx + 1)
        elif i == 1:
            back_tracking(temp_sum - nums[num_idx + 1], num_idx + 1)
        elif i == 2:
            back_tracking(temp_sum * nums[num_idx + 1], num_idx + 1)
        else:
            if temp_sum < 0:
                back_tracking(-(-temp_sum // nums[num_idx + 1]), num_idx + 1)
            else:
                back_tracking(temp_sum // nums[num_idx + 1], num_idx + 1)
        commands[i] += 1

    return


back_tracking(nums[0], 0)

print(max_answer)
print(min_answer)
