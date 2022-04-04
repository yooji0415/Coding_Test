def solution(arr):
    answer = 0
    sum = 0
    for item in arr:
        sum += item
    return sum / len(arr)