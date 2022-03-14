import sys

test_case = int(sys.stdin.readline())
for _ in range(test_case):
    doc = []
    n, target = map(int, sys.stdin.readline().split())
    temp = list(map(int, sys.stdin.readline().split()))
    for i in range(n):
        doc.append([temp[i], i])

    cnt = 1
    while doc:
        max_num = max(doc, key=lambda x: x[0])
        out = doc.index(max_num)
        temp = doc[out:] + doc[:out]
        doc = temp
        if doc[0][1] == target:
            print(cnt)
            break
        else:
            doc.pop(0)

        cnt += 1
