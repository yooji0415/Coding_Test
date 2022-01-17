n = int(input())
a = list(map(int, input().split()))
a.sort()
m = int(input())
test_list = list(map(int, input().split()))
for test in test_list:
    start = 0
    end = len(a) - 1
    while start <= end:
        mid = (start + end)//2
        if a[mid] == test:
            print(1)
            break
        elif a[mid] < test:
            start = mid + 1
        else:
            end = mid - 1

    if start > end:
        print(0)
