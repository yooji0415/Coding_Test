def solution(A, B):
    answer = 0
    A.sort(reverse=True)
    B.sort()
    for i in range(len(A)):
        answer += A[i] * B[i]

    return answer


# 모범답안
# zip 을 이용한 더 간단한 풀이이다.
def getMinSum(A,B):
    return sum(a*b for a, b in zip(sorted(A), sorted(B, reverse = True)))
