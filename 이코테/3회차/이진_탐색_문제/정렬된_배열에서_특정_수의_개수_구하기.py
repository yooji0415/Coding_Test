def solution(N, x, array):
    def find_left(left, right):
        if left > right:
            return None
        mid = (left + right) // 2
        if array[mid] == x and (mid == 0 or array[mid - 1] < x):
            return mid
        if array[mid] < x:
            return find_left(mid + 1, right)
        if array[mid] >= x:
            return find_left(left, mid - 1)

    def find_right(left, right):
        if left > right:
            return None
        mid = (left + right) // 2
        if array[mid] == x and (mid == len(array) - 1 or array[mid + 1] > x):
            return mid
        if array[mid] <= x:
            return find_right(mid + 1, right)
        if array[mid] > x:
            return find_right(left, mid - 1)

    def get_cnt():
        left = find_left(0, len(array) - 1)
        if not left:
            return -1
        right = find_right(0, len(array) - 1)
        return right - left + 1

    return get_cnt()


print(solution(7, 2, [1, 1, 2, 2, 2, 2, 3]))
print(solution(7, 4, [1, 1, 2, 2, 2, 2, 3]))
