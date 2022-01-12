# 에라토스테네스의 체 사용
n = 10000
# 0과 1을 제외한 수는 일단 True 설정
is_prime = [False, False] + [True]*(n-1)
for i in range(2, n+1):
    if is_prime[i]:
        for j in range(2*i, n+1, i):
            is_prime[j] = False


test_case = int(input())
# 소수를 담아서 덧샘 짝을 찾는다
for test in range(test_case):
    test_num = int(input())
    answer_list = []
    for num in range(2, test_num//2 + 1):
        if is_prime[num] and is_prime[test_num - num]:
            answer_list = [num, test_num - num]

    print("{} {}".format(answer_list[0], answer_list[1]))

