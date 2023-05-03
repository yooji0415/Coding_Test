def solution(N, array):
    def find(left, right):
        if left > right:
            return -1

        mid = (left + right) // 2
        if array[mid] == mid:
            return mid
        if array[mid] < mid:
            return find(mid + 1, right)
        else:
            return find(left, mid - 1)
    return find(0, len(array) - 1)


print(solution(5, [-15, -6, 1, 3, 7]))
print(solution(7, [-15, -4, 2, 8, 9, 13, 15]))
print(solution(7, [-15, -4, 3, 8, 9, 13, 15]))
