def solution(n, arr1, arr2):
    binary_arr1 = []
    binary_arr2 = []
    answer = []
    for n1, n2 in zip(arr1, arr2):
        cn1 = bin(n1)[2:]
        while len(cn1) < n:
            cn1 = "0" + cn1

        cn2 = bin(n2)[2:]
        while len(cn2) < n:
            cn2 = "0" + cn2

        binary_arr1.append(list(cn1))
        binary_arr2.append(list(cn2))

    for list1, list2 in zip(binary_arr1, binary_arr2):
        temp = ""
        for n1, n2 in zip(list1, list2):
            if n1 == "1" or n2 == "1":
                temp = temp + "#"
            else:
                temp = temp + " "

        answer.append(temp)
    return answer


# 모범답안
# 위 알고리즘을 파이썬 내장함수를 이용해서 상당히 간결하게 처리함
def best_solution(n, arr1, arr2):
    answer = []
    for i, j in zip(arr1, arr2):
        a12 = str(bin(i | j)[2:])
        a12=a12.rjust(n, '0')
        a12=a12.replace('1', '#')
        a12=a12.replace('0', ' ')
        answer.append(a12)
    return answer
