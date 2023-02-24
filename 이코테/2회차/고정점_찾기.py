def binary_search(array, start, end):
    if start > end:
        return None

    mid = (start + end) // 2
    if mid == array[mid]:
        return mid

    # 인덱스 보다 어레이의 값이 작다 => 오른쪽으로!
    # -2 -1 0 3 4
    if mid > array[mid]:
        return binary_search(array, mid + 1, end)

    return binary_search(array, start, mid - 1)


n = int(input())
array = list(map(int, input().split()))
answer = binary_search(array, 0, n - 1)

print(-1 if answer is None else answer)
