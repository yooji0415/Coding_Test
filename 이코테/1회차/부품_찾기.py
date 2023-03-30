import sys

n = int(sys.stdin.readline().rstrip())
items = list(map(int, sys.stdin.readline().rstrip().split()))
m = int(sys.stdin.readline().rstrip())
targets = list(map(int, sys.stdin.readline().rstrip().split()))

items.sort()


def search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return None


for target in targets:
    result = search(items, target, 0, n - 1)
    if result:
        print('yes', end=" ")
    else:
        print('no', end=" ")
