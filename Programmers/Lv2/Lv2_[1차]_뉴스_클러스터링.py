def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    list1 = []
    list2 = []
    for i in range(len(str1) - 1):
        if str1[i:i + 2].isalpha():
            list1.append(str1[i:i + 2])
    for i in range(len(str2) - 1):
        if str2[i:i + 2].isalpha():
            list2.append(str2[i:i + 2])
    # 원소가 없는 경우 먼저 처리해준다.
    len1 = len(list1)
    len2 = len(list2)
    if len1 + len2 == 0:
        return 65536
    if len1 == 0 or len2 == 0:
        return 0
    # 교집합, 합집합 원소 수를 구한다.
    c = 0
    for l in list1:
        if l in list2:
            c += 1
            list2.pop(list2.index(l))
            len2 -= 1
            if len2 == 0:
                break

    return int(65536 * c / (len1 + len2))