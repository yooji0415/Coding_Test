n = int(input())
array = list(map(int, input().split()))


def find(start, end):
    if start > end:
        return -1
    mid = (start + end) // 2

    if mid == array[mid]:
        return mid

    if mid < array[mid]:
        return find(start, mid + 1)

    if mid > array[mid]:
        return find(mid + 1, end)


print(find(0, len(array) - 1))
