# 7 2
# 1 1 2 2 2 2 3
def count_by_value(array, target):
    first_idx = first(array, target, 0, n - 1)
    if first_idx is None:
        return 0

    last_idx = last(array, target, 0, n - 1)
    return last_idx - first_idx + 1


def first(array, target, start, end):
    if start > end:
        return None

    mid = (start + end) // 2
    if (mid == 0 or target > array[mid - 1]) and array[mid] == target:
        return mid

    if target <= array[mid]:
        return first(array, target, start, mid - 1)

    return first(array, target, mid + 1, end)


def last(array, target, start, end):
    if start > end:
        return None

    mid = (start + end) // 2

    if (mid == n - 1 or target < array[mid + 1]) and array[mid] == target:
        return mid

    if target < array[mid]:
        return last(array, target, start, mid - 1)

    return last(array, target, mid + 1, end)


n, target = map(int, input().split())
array = list(map(int, input().split()))

answer = count_by_value(array, target)
print(-1 if answer == 0 else answer)
